"""Procedural ambience/SFX generator for 《白雨》 — pure stdlib."""
import math, random, wave, struct, os

SR = 22050
OUT = r"C:\Users\Administrator\Desktop\game\game\audio"
os.makedirs(OUT, exist_ok=True)
random.seed(20260917)


def write(name, samples, peak=0.7):
    m = max(1e-9, max(abs(s) for s in samples))
    g = peak / m
    data = b"".join(struct.pack("<h", int(max(-1.0, min(1.0, s * g)) * 32767)) for s in samples)
    with wave.open(os.path.join(OUT, name), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data)
    print(f"{name:18s} {len(samples)/SR:5.1f}s  {len(data)/1024:6.0f} KB")


def noise(n):
    return [random.uniform(-1.0, 1.0) for _ in range(n)]


def lowpass(x, a):
    y = 0.0
    out = []
    for v in x:
        y += a * (v - y)
        out.append(y)
    return out


def highpass(x, a):
    y = 0.0
    out = []
    for v in x:
        y += a * (v - y)
        out.append(v - y)
    return out


def envelope(n, attack, decay, floor=0.0):
    a = int(attack * SR) or 1
    d = max(1, int(decay * SR))
    return [min(1.0, i / a) * math.exp(-i / d) * (1 - floor) + floor for i in range(n)]


def crossfade_loop(x, sec=1.5):
    n = int(sec * SR)
    if len(x) <= 3 * n:
        return x
    body = x[:-n]
    for i in range(n):
        t = i / n
        body[i] = body[i] * t + x[len(x) - n + i] * (1 - t)
    return body


def rain(dur, cutoff, drops, level=1.0):
    n = int(dur * SR)
    base = lowpass(noise(n), cutoff)
    # a second, brighter layer
    bright = highpass(lowpass(noise(n), 0.55), 0.12)
    mix = [base[i] * 0.8 + bright[i] * 0.18 for i in range(n)]
    # droplets
    for _ in range(drops):
        at = random.randrange(0, n - 400)
        f = random.uniform(1800, 4200)
        ln = random.randint(120, 420)
        amp = random.uniform(0.05, 0.18)
        for j in range(ln):
            mix[at + j] += amp * math.exp(-j / (ln * 0.25)) * math.sin(2 * math.pi * f * j / SR)
    # slow swell
    for i in range(n):
        mix[i] *= (0.85 + 0.15 * math.sin(2 * math.pi * i / (SR * 13.0)))
    return crossfade_loop(mix)


def thunder(dur=5.0):
    n = int(dur * SR)
    brown = []
    v = 0.0
    for _ in range(n):
        v = max(-1, min(1, v + random.uniform(-0.06, 0.06)))
        brown.append(v)
    rumble = lowpass(brown, 0.02)
    env = envelope(n, 0.06, 1.6)
    crack = lowpass(noise(n), 0.75)
    out = [rumble[i] * env[i] * 3.2 + crack[i] * env[i] * env[i] * 0.35 for i in range(n)]
    # roll trail
    for i in range(n):
        if i > SR * 1.2:
            out[i] *= math.exp(-(i - SR * 1.2) / (SR * 2.2))
    return out


def thump(dur, f0, f1):
    n = int(dur * SR)
    out = []
    ph = 0.0
    for i in range(n):
        t = i / n
        f = f0 + (f1 - f0) * t
        ph += 2 * math.pi * f / SR
        e = math.exp(-t * 9) * (1 - math.exp(-i / 60))
        out.append(math.sin(ph) * e)
    return out


def knock():
    n = int(2.1 * SR)
    out = [0.0] * n
    for t0 in (0.0, 0.55, 1.12):
        s = int(t0 * SR)
        k = thump(0.22, 130, 55)
        c = lowpass(noise(len(k)), 0.7)
        for i, v in enumerate(k):
            if s + i < n:
                out[s + i] += v * 0.9 + c[i] * 0.25 * math.exp(-i / 300)
    return out


def creak():
    n = int(1.6 * SR)
    out = []
    ph = 0.0
    for i in range(n):
        t = i / n
        f = 220 + 160 * math.sin(t * 9) + 40 * math.sin(t * 40)
        ph += 2 * math.pi * f / SR
        e = math.sin(math.pi * t) ** 1.5
        out.append((math.sin(ph) * 0.25 + random.uniform(-0.08, 0.08)) * e)
    return lowpass(out, 0.4)


def suitcase():
    n = int(2.6 * SR)
    base = lowpass(noise(n), 0.06)
    out = []
    for i in range(n):
        t = i / SR
        mod = 0.55 + 0.45 * math.sin(2 * math.pi * 7.5 * t)
        e = min(1.0, t / 0.15) * min(1.0, (n - i) / (0.4 * SR))
        out.append(base[i] * mod * e * 2.2)
    return out


def tv(dur=18.0):
    """Muffled news: syllabic band-limited noise, unintelligible on purpose."""
    n = int(dur * SR)
    src = lowpass(noise(n), 0.35)
    src = highpass(src, 0.02)
    out = [0.0] * n
    i = 0
    while i < n:
        ln = random.randint(int(0.09 * SR), int(0.28 * SR))
        amp = random.uniform(0.25, 0.9)
        gap = random.randint(int(0.02 * SR), int(0.09 * SR))
        for j in range(ln):
            if i + j >= n:
                break
            t = j / ln
            e = math.sin(math.pi * t) ** 0.6
            f = random.uniform(90, 150)  # formant-ish wobble
            out[i + j] = src[i + j] * amp * e * (0.6 + 0.4 * math.sin(2 * math.pi * f * j / SR))
        i += ln + gap
    # telephone/room tone
    for i in range(n):
        out[i] += 0.008 * math.sin(2 * math.pi * 60 * i / SR)
    return out


def heartbeat():
    n = int(2.2 * SR)
    out = [0.0] * n
    for t0, a in ((0.0, 1.0), (0.34, 0.7)):
        s = int(t0 * SR)
        k = thump(0.28, 90, 40)
        for i, v in enumerate(k):
            if s + i < n:
                out[s + i] += v * a
    return out


def flash():
    n = int(1.1 * SR)
    out = []
    ph = 0.0
    for i in range(n):
        t = i / n
        f = 3000 * math.exp(-t * 4) + 120
        ph += 2 * math.pi * f / SR
        e = math.exp(-t * 6)
        out.append((math.sin(ph) * 0.5 + random.uniform(-0.4, 0.4)) * e)
    return lowpass(out, 0.9)


def bgm(dur=64.0):
    """Slow, cold ambient pad + sparse pentatonic notes."""
    n = int(dur * SR)
    out = [0.0] * n

    def note(start, freq, length, amp, attack=0.8):
        s = int(start * SR)
        ln = int(length * SR)
        for j in range(ln):
            if s + j >= n:
                break
            t = j / ln
            e = min(1.0, (j / SR) / attack) * (1 - t) ** 1.7
            out[s + j] += amp * e * math.sin(2 * math.pi * freq * j / SR + 0.3 * math.sin(2 * math.pi * 0.2 * j / SR))

    # pad: A2 + E3 + C4 with slow beating
    pad = [110.0, 164.81, 261.63, 329.63]
    for f in pad:
        for k in range(4):
            start = k * 16.0
            note(start, f, 20.0, 0.10)
            note(start + 0.5, f * 1.003, 20.0, 0.06)

    # sparse melody
    melody = [440.0, 523.25, 392.0, 329.63, 587.33, 440.0, 392.0]
    t = 6.0
    idx = 0
    while t < dur - 6:
        note(t, melody[idx % len(melody)], 5.5, 0.10, attack=0.05)
        t += random.choice([5.0, 6.5, 8.0])
        idx += 1

    # airy noise bed
    bed = lowpass(noise(n), 0.02)
    for i in range(n):
        out[i] += bed[i] * 0.05
    return crossfade_loop(out, 2.0)


write("rain_loop.wav", rain(32, 0.30, 260), 0.55)
write("rain_heavy.wav", rain(24, 0.20, 180), 0.62)
write("thunder.wav", thunder(), 0.85)
write("knock.wav", knock(), 0.80)
write("door_creak.wav", creak(), 0.45)
write("suitcase.wav", suitcase(), 0.55)
write("tv.wav", tv(), 0.28)
write("heartbeat.wav", heartbeat(), 0.75)
write("flash.wav", flash(), 0.55)
write("bgm.wav", bgm(), 0.42)
print("done")
