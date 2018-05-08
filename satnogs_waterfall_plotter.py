#!/usr/bin/env python
from __future__ import print_function
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys

# Get filename
fname=sys.argv[1]
if len(sys.argv)==3:
    outfname=sys.argv[2]
else:
    outfname=fname.replace("receiving_","").replace(".dat",".png")

# Open file
f=open(fname)

# Read number of channels
nchan=int(np.fromfile(f,dtype='float32',count=1)[0])

# Read channel frequencies
freq=np.fromfile(f,dtype='float32',count=nchan)/1000.0

# Read entire file
data=np.fromfile(f,dtype='float32').reshape(-1,nchan+1)

# Close file
f.close()

# Get time
t=data[:,:1]

# Get spectra
spec=data[:,1:]

# Get extrema
fmin,fmax=np.min(freq),np.max(freq)
tmin,tmax=np.min(t),np.max(t)

# Set dynamic range
c=spec>-200.0
if np.sum(c)>100:
    vmin=np.mean(spec[c])-2.0*np.std(spec[c])
    vmax=np.mean(spec[c])+6.0*np.std(spec[c])
else:
    vmin=-100
    vmax=-50
    
cmap="jet"
print("%s %.2f %.2f %.2f %.2f %.2f"%(fname,np.mean(spec[c]),np.median(spec[c]),np.std(spec[c]),vmin,vmax))

# Make plot
plt.figure(figsize=(10,20))
plt.imshow(spec,origin='lower',aspect='auto',interpolation='None',extent=[fmin,fmax,tmin,tmax],vmin=vmin,vmax=vmax,cmap=cmap)
plt.xlabel("Frequency (kHz)")
plt.ylabel("Time (seconds)")
fig=plt.colorbar(aspect=50)
fig.set_label("Power (dB)")
plt.savefig(outfname,bbox_inches='tight')
