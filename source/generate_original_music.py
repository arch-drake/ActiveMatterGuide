from pathlib import Path
import numpy as np, subprocess, json
out=Path(__file__).resolve().parent.parent / 'assets' / 'music'
out.mkdir(parents=True,exist_ok=True)
sr=22050; duration=32; n=sr*duration
t=np.arange(n,dtype=np.float32)/sr
modes={
'dead_relay': dict(bpm=88, root=45, chord=[0,3,7,10], motion=[0,7,10,3,5,10,7,3],noise=.010,percuss=.030),
'monolith_dream': dict(bpm=72,root=48,chord=[0,4,7,11],motion=[0,4,7,11,7,4,2,7],noise=.004,percuss=.012),
'red_zone':dict(bpm=112,root=38,chord=[0,3,6,10],motion=[0,6,3,10,0,7,6,3],noise=.011,percuss=.075),
'glass_reactor':dict(bpm=96,root=50,chord=[0,2,7,9],motion=[0,7,9,2,4,9,7,2],noise=.008,percuss=.024),
'dawn_after_extraction':dict(bpm=80,root=47,chord=[0,4,7,9],motion=[0,4,7,12,9,7,4,7],noise=.004,percuss=.016)
}
for idx,(name,params) in enumerate(modes.items()):
    freq=lambda m: 440.0*2**((m-69)/12)
    root=params['root']; chord=params['chord']; rng=np.random.default_rng(20261020+idx)
    x=np.zeros(n,dtype=np.float32)
    # Two gently modulated pad voices with a slow attack and gentle motion.
    for j,degree in enumerate(chord):
        f=freq(root+degree+12)
        slow=np.sin(2*np.pi*(.025+.008*j)*t+j*1.3)
        tone=(np.sin(2*np.pi*f*t+(.23+.06*j)*slow)+.18*np.sin(2*np.pi*2*f*t+.16*slow))
        amp=.048 + .017*np.sin(2*np.pi*(.012+j*.004)*t+j)
        x+=np.asarray(tone*amp,dtype=np.float32)
    step_seconds=60.0/params['bpm']/2
    steps=int(duration/step_seconds)+1
    for k in range(steps):
        pos=k*step_seconds; start=int(pos*sr)
        if start>=n:break
        count=min(int(step_seconds*sr*1.65),n-start)
        if count<1:continue
        u=np.arange(count,dtype=np.float32)/sr
        f=freq(root+12+params['motion'][k%len(params['motion'])])
        env=(1-np.exp(-u*22))*np.exp(-u*(4 if name=='red_zone' else 3.2))
        wave=np.sin(2*np.pi*f*u+.15*np.sin(2*np.pi*1.2*u))+.26*np.sin(2*np.pi*2.01*f*u)
        x[start:start+count]+=(.08 if name=='red_zone' else .054)*env*wave
        if k%2==0:
            lowf=50 if name=='red_zone' else 39
            bump=.05*np.exp(-u*14)*np.sin(2*np.pi*(lowf*u+12*(1-np.exp(-u*20))/20))
            x[start:start+count]+=params['percuss']*bump*6
    # Filtered low-volume texture
    noise=rng.standard_normal(n).astype('float32')
    smooth=np.convolve(noise,np.ones(80,dtype=np.float32)/80,mode='same')
    x+=params['noise']*smooth
    # seamless-sounding crossfade ends; remove DC and leave headroom
    fades=int(sr*.45)
    x[:fades]*=np.linspace(0,1,fades,dtype=np.float32)
    x[-fades:]*=np.linspace(1,0,fades,dtype=np.float32)
    x=np.tanh(x*1.7).astype(np.float32)
    raw=out/(name+'.f32')
    raw.write_bytes(x.tobytes())
    mp3=out/(name+'.mp3')
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(sr),'-ac','1','-i',str(raw),'-codec:a','libmp3lame','-b:a','64k',str(mp3)],check=True)
    raw.unlink()
    print(name,mp3.stat().st_size)
