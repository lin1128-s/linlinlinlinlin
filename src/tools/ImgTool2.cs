using System;
using System.Drawing;
using System.Drawing.Imaging;

public static class ImgTool2
{
    public static string TrimAlpha(string src, string dst, int margin = 6)
    {
        using (var s = new Bitmap(src))
        {
            int w = s.Width, h = s.Height;
            var bmp = new Bitmap(w, h, PixelFormat.Format32bppArgb);
            using (var g = Graphics.FromImage(bmp)) g.DrawImage(s, 0, 0);
            var d = bmp.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadOnly, PixelFormat.Format32bppArgb);
            var px = new byte[w * h * 4];
            System.Runtime.InteropServices.Marshal.Copy(d.Scan0, px, 0, px.Length);
            bmp.UnlockBits(d);

            int minX = w, minY = h, maxX = -1, maxY = -1;
            for (int y = 0; y < h; y++)
                for (int x = 0; x < w; x++)
                    if (px[(y * w + x) * 4 + 3] > 8)
                    {
                        if (x < minX) minX = x; if (x > maxX) maxX = x;
                        if (y < minY) minY = y; if (y > maxY) maxY = y;
                    }
            if (maxX < 0) { minX = 0; minY = 0; maxX = w - 1; maxY = h - 1; }
            minX = Math.Max(0, minX - margin); minY = Math.Max(0, minY - margin);
            maxX = Math.Min(w - 1, maxX + margin); maxY = Math.Min(h - 1, maxY + margin);
            int cw = maxX - minX + 1, ch = maxY - minY + 1;
            using (var outBmp = new Bitmap(cw, ch, PixelFormat.Format32bppArgb))
            {
                using (var g = Graphics.FromImage(outBmp))
                    g.DrawImage(bmp, new Rectangle(0, 0, cw, ch), new Rectangle(minX, minY, cw, ch), GraphicsUnit.Pixel);
                outBmp.Save(dst, ImageFormat.Png);
            }
            bmp.Dispose();
            return cw + "x" + ch;
        }
    }
}
