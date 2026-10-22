using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.Collections.Generic;

public static class ImgTool
{
    // ---------- helpers ----------
    static int Lum(int r, int g, int b) { return (r * 299 + g * 587 + b * 114) / 1000; }

    static Bitmap Load32(string path)
    {
        using (var src = new Bitmap(path))
        {
            var bmp = new Bitmap(src.Width, src.Height, PixelFormat.Format32bppArgb);
            using (var g = Graphics.FromImage(bmp)) { g.DrawImage(src, 0, 0, src.Width, src.Height); }
            return bmp;
        }
    }

    // ---------- white background removal with flood fill ----------
    public static string RemoveWhiteBg(string src, string dst, int hard = 244, int soft = 234)
    {
        using (var bmp = Load32(src))
        {
            int w = bmp.Width, h = bmp.Height, n = w * h;
            var data = bmp.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadOnly, PixelFormat.Format32bppArgb);
            var px = new byte[n * 4];
            System.Runtime.InteropServices.Marshal.Copy(data.Scan0, px, 0, px.Length);
            bmp.UnlockBits(data);

            var bg = new bool[n];
            var q = new Queue<int>();
            for (int x = 0; x < w; x++)
            {
                TrySeed(px, bg, q, x, w);
                TrySeed(px, bg, q, (h - 1) * w + x, w);
            }
            for (int y = 0; y < h; y++)
            {
                TrySeed(px, bg, q, y * w, w);
                TrySeed(px, bg, q, y * w + w - 1, w);
            }
            while (q.Count > 0)
            {
                int i = q.Dequeue();
                int x = i % w, y = i / w;
                if (x > 0) TrySeed(px, bg, q, i - 1, w);
                if (x < w - 1) TrySeed(px, bg, q, i + 1, w);
                if (y > 0) TrySeed(px, bg, q, i - w, w);
                if (y < h - 1) TrySeed(px, bg, q, i + w, w);
            }

            // soft edge: eat 2px into near-white surroundings
            for (int pass = 0; pass < 2; pass++)
            {
                var add = new List<int>();
                for (int i = 0; i < n; i++)
                {
                    if (bg[i]) continue;
                    if (px[i * 4 + 3] == 0) continue;
                    int l = Lum(px[i * 4], px[i * 4 + 1], px[i * 4 + 2]);
                    if (l < soft) continue;
                    int x = i % w, y = i / w;
                    if ((x > 0 && bg[i - 1]) || (x < w - 1 && bg[i + 1]) ||
                        (y > 0 && bg[i - w]) || (y < h - 1 && bg[i + w])) add.Add(i);
                }
                foreach (int i in add) bg[i] = true;
            }

            var alpha = new byte[n];
            for (int i = 0; i < n; i++)
            {
                if (bg[i]) { alpha[i] = 0; continue; }
                int l = Lum(px[i * 4], px[i * 4 + 1], px[i * 4 + 2]);
                alpha[i] = l > 250 ? (byte)140 : (byte)255;
            }

            // 3x3 box blur of alpha, but only where pixel is light (line art stays crisp)
            var blur = new byte[n];
            for (int y = 0; y < h; y++)
            {
                for (int x = 0; x < w; x++)
                {
                    int i = y * w + x;
                    int l = Lum(px[i * 4], px[i * 4 + 1], px[i * 4 + 2]);
                    if (bg[i] || l < 210) { blur[i] = alpha[i]; continue; }
                    int sum = 0, cnt = 0;
                    for (int dy = -1; dy <= 1; dy++)
                        for (int dx = -1; dx <= 1; dx++)
                        {
                            int xx = x + dx, yy = y + dy;
                            if (xx < 0 || yy < 0 || xx >= w || yy >= h) continue;
                            sum += alpha[yy * w + xx]; cnt++;
                        }
                    blur[i] = (byte)(sum / cnt);
                }
            }
            alpha = blur;

            // bounding box
            int minX = w, minY = h, maxX = -1, maxY = -1;
            for (int y = 0; y < h; y++)
                for (int x = 0; x < w; x++)
                {
                    if (alpha[y * w + x] > 8)
                    {
                        if (x < minX) minX = x; if (x > maxX) maxX = x;
                        if (y < minY) minY = y; if (y > maxY) maxY = y;
                    }
                }
            if (maxX < 0) { minX = 0; minY = 0; maxX = w - 1; maxY = h - 1; }
            int m = 6;
            minX = Math.Max(0, minX - m); minY = Math.Max(0, minY - m);
            maxX = Math.Min(w - 1, maxX + m); maxY = Math.Min(h - 1, maxY + m);

            int cw = maxX - minX + 1, ch = maxY - minY + 1;
            using (var outBmp = new Bitmap(cw, ch, PixelFormat.Format32bppArgb))
            {
                var od = outBmp.LockBits(new Rectangle(0, 0, cw, ch), ImageLockMode.WriteOnly, PixelFormat.Format32bppArgb);
                var op = new byte[cw * ch * 4];
                for (int y = 0; y < ch; y++)
                    for (int x = 0; x < cw; x++)
                    {
                        int si = (y + minY) * w + (x + minX);
                        int di = (y * cw + x) * 4;
                        op[di] = px[si * 4]; op[di + 1] = px[si * 4 + 1];
                        op[di + 2] = px[si * 4 + 2]; op[di + 3] = alpha[si];
                    }
                System.Runtime.InteropServices.Marshal.Copy(op, 0, od.Scan0, op.Length);
                outBmp.UnlockBits(od);
                outBmp.Save(dst, ImageFormat.Png);
            }
            return cw + "x" + ch;
        }
    }

    static void TrySeed(byte[] px, bool[] bg, Queue<int> q, int i, int w)
    {
        if (bg[i]) return;
        if (px[i * 4 + 3] == 0) { bg[i] = true; q.Enqueue(i); return; }
        int l = Lum(px[i * 4], px[i * 4 + 1], px[i * 4 + 2]);
        if (l >= 244) { bg[i] = true; q.Enqueue(i); }
    }

    // ---------- background: crop to 1920x1080 (removes watermark strip) ----------
    public static void MakeBg(string src, string dst)
    {
        using (var bmp = new Bitmap(src))
        using (var outBmp = new Bitmap(1920, 1080, PixelFormat.Format24bppRgb))
        using (var g = Graphics.FromImage(outBmp))
        {
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;
            g.PixelOffsetMode = PixelOffsetMode.HighQuality;
            g.DrawImage(bmp, new Rectangle(0, 0, 1920, 1080), new Rectangle(64, 0, 1920, 1080), GraphicsUnit.Pixel);
            SaveJpeg(outBmp, dst, 93);
        }
    }

    static void SaveJpeg(Bitmap bmp, string path, long quality)
    {
        var enc = ImageCodecInfo.GetImageEncoders();
        var ep = new EncoderParameters(1);
        ep.Param[0] = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, quality);
        ImageCodecInfo jpg = null;
        foreach (var e in enc) if (e.MimeType == "image/jpeg") jpg = e;
        bmp.Save(path, jpg, ep);
    }

    // ---------- rain particle ----------
    public static void MakeRainDrop(string path)
    {
        int w = 6, h = 64;
        using (var bmp = new Bitmap(w, h, PixelFormat.Format32bppArgb))
        {
            for (int y = 0; y < h; y++)
            {
                double a = Math.Sin(Math.PI * y / (h - 1));
                int alpha = (int)(70 * a);
                for (int x = 0; x < w; x++)
                {
                    double dx = Math.Abs(x - (w - 1) / 2.0) / ((w - 1) / 2.0);
                    int aa = (int)(alpha * (1 - dx));
                    bmp.SetPixel(x, y, Color.FromArgb(Math.Max(0, aa), 230, 240, 255));
                }
            }
            bmp.Save(path, ImageFormat.Png);
        }
    }

    // ---------- vignette ----------
    public static void MakeVignette(string path)
    {
        int w = 1920, h = 1080;
        using (var bmp = new Bitmap(w, h, PixelFormat.Format32bppArgb))
        {
            using (var g = Graphics.FromImage(bmp))
            using (var p = new GraphicsPath())
            {
                var rect = new Rectangle(0, 0, w, h);
                p.AddEllipse(-w / 4, -h / 4, w + w / 2, h + h / 2);
                using (var brush = new PathGradientBrush(p))
                {
                    brush.CenterColor = Color.FromArgb(0, 0, 0, 0);
                    brush.SurroundColors = new Color[] { Color.FromArgb(210, 0, 0, 0) };
                    brush.FocusScales = new PointF(0.55f, 0.45f);
                    g.FillRectangle(brush, rect);
                }
            }
            bmp.Save(path, ImageFormat.Png);
        }
    }

    // ---------- sticky note ----------
    public static void MakeStickyNote(string path)
    {
        int w = 880, h = 600;
        using (var bmp = new Bitmap(w, h, PixelFormat.Format32bppArgb))
        using (var g = Graphics.FromImage(bmp))
        {
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            g.Clear(Color.Transparent);

            g.TranslateTransform(w / 2f, h / 2f);
            g.RotateTransform(-2.4f);
            g.TranslateTransform(-w / 2f, -h / 2f);

            var paper = new Rectangle(20, 30, w - 60, h - 80);
            using (var shadow = new SolidBrush(Color.FromArgb(26, 0, 0, 0)))
                g.FillRectangle(shadow, new Rectangle(paper.X + 8, paper.Y + 10, paper.Width, paper.Height));
            using (var grad = new LinearGradientBrush(paper, Color.FromArgb(255, 249, 232, 190), Color.FromArgb(255, 240, 220, 165), 90f))
                g.FillRectangle(grad, paper);
            using (var pen = new Pen(Color.FromArgb(35, 120, 100, 60), 1f))
                g.DrawRectangle(pen, paper);

            // tape
            using (var tape = new SolidBrush(Color.FromArgb(95, 255, 255, 255)))
            {
                g.TranslateTransform(paper.X + 40, paper.Y - 6);
                g.RotateTransform(-8);
                g.FillRectangle(tape, 0, 0, 150, 34);
                g.ResetTransform();
                g.TranslateTransform(paper.Right - 190, paper.Y - 10);
                g.RotateTransform(6);
                g.FillRectangle(tape, 0, 0, 150, 34);
                g.ResetTransform();
            }
            g.ResetTransform();
            g.TranslateTransform(w / 2f, h / 2f);
            g.RotateTransform(-2.4f);
            g.TranslateTransform(-w / 2f, -h / 2f);

            var ink = Color.FromArgb(255, 58, 68, 92);
            using (var f = new Font("KaiTi", 46, FontStyle.Regular, GraphicsUnit.Pixel))
            using (var b = new SolidBrush(ink))
            {
                g.DrawString("早上第一节有课，", f, b, 78, 100);
                g.DrawString("别又不吃早饭。", f, b, 78, 178);
                using (var f2 = new Font("KaiTi", 52, FontStyle.Regular, GraphicsUnit.Pixel))
                    g.DrawString("—— 雨", f2, b, 420, 270);
            }

            // rabbit doodle
            using (var pen = new Pen(ink, 3f))
            {
                pen.StartCap = LineCap.Round; pen.EndCap = LineCap.Round;
                int rx = 175, ry = 390;
                g.DrawEllipse(pen, rx, ry + 26, 74, 66);
                g.DrawEllipse(pen, rx + 12, ry - 30, 16, 52);
                g.DrawEllipse(pen, rx + 44, ry - 30, 16, 52);
                g.FillEllipse(new SolidBrush(ink), rx + 20, ry + 50, 5, 5);
                g.FillEllipse(new SolidBrush(ink), rx + 48, ry + 50, 5, 5);
                g.DrawArc(pen, rx + 30, ry + 56, 14, 10, 20, 140);
            }
            // pig doodle
            using (var pen = new Pen(ink, 3f))
            {
                pen.StartCap = LineCap.Round; pen.EndCap = LineCap.Round;
                int px = 330, py = 392;
                g.DrawEllipse(pen, px, py + 20, 86, 62);
                g.DrawEllipse(pen, px + 22, py + 40, 42, 26);
                g.FillEllipse(new SolidBrush(ink), px + 38, py + 50, 5, 5);
                g.FillEllipse(new SolidBrush(ink), px + 48, py + 50, 5, 5);
                g.FillEllipse(new SolidBrush(ink), px + 16, py + 32, 5, 5);
                g.FillEllipse(new SolidBrush(ink), px + 66, py + 32, 5, 5);
                g.DrawLine(pen, px + 4, py + 26, px + 14, py + 6);
                g.DrawLine(pen, px + 82, py + 26, px + 72, py + 6);
            }
            // heart
            using (var pen = new Pen(Color.FromArgb(255, 190, 90, 90), 3f))
            {
                int hx = 520, hy = 400;
                g.DrawArc(pen, hx, hy, 26, 26, 180, 180);
                g.DrawArc(pen, hx + 24, hy, 26, 26, 180, 180);
                g.DrawLine(pen, hx, hy + 14, hx + 25, hy + 46);
                g.DrawLine(pen, hx + 50, hy + 14, hx + 25, hy + 46);
            }
            bmp.Save(path, ImageFormat.Png);
        }
    }

    // ---------- paper texture for poem card? ----------
    public static void MakeGrain(string path, int w, int h)
    {
        var rnd = new Random(20260917);
        using (var bmp = new Bitmap(w, h, PixelFormat.Format32bppArgb))
        {
            for (int y = 0; y < h; y++)
                for (int x = 0; x < w; x++)
                {
                    int v = rnd.Next(0, 255);
                    int a = rnd.Next(0, 12);
                    bmp.SetPixel(x, y, Color.FromArgb(a, v, v, v));
                }
            bmp.Save(path, ImageFormat.Png);
        }
    }
}
