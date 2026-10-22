import wave, struct, math, os
d = r"C:\Users\Administrator\Desktop\game\game\audio"
for f in sorted(os.listdir(d)):
    w = wave.open(os.path.join(d,f))
    n = w.getnframes(); data = w.readframes(n)
    s = struct.unpack("<%dh" % n, data)
    rms = math.sqrt(sum(v*v for v in s)/n)/32768
    peak = max(abs(v) for v in s)/32768
    zc = sum(1 for i in range(1,n) if (s[i-1]<0)!=(s[i]<0))/ (n/22050)
    print(f"{f:16s} rms={rms:.3f} peak={peak:.2f} zcr={zc:6.0f}/s")
