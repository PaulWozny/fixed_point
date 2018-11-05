
import numpy as np
import matplotlib.pyplot as plt

from fixed_point import fixed,W
from fixed_point import ROUND_MODES

format = W(4,0,3)
for rm in ROUND_MODES:
    xf = np.arange(-1200,1200)/1000.
    xq,xe = ([],[])
    for ff in xf:
        fx = float(fixed(ff, format=format, round_mode=rm))
        xq.append(fx)    # back to float for plotting, preserves value
        xe.append(ff-fx) # also plot error

    # plot the quantized values
    fig,ax = plt.subplots(1)
    tax = ax.twinx()
    ax.plot(xf,xf, label='real number value')
    ax.plot(xf,xq, label='quantized value')
    ax.grid(True)
    ax.set_xlim(-1.2,1.2)
    ax.set_ylim(-1.2,1.2)
    ax.set_title("Quantization\nfixed(format=W%s,"
              "round_mode='%s'"
              "overflow_mode='saturate')"%(rm,W.format))
    ax.set_ylabel('')
    ax.set_xlabel('')

    tax.plot(xf,xe, 'm:', alpha=.6, label='error')    
    xf = np.array(xf)
    xq = np.array(xq)
    x1,x2 = (xf == -.75).nonzero()[0][0],(xf == .75).nonzero()[0][0]
    xe = np.array(xe)
    tax.axhline(np.mean(xe[x1:x2]), 0, len(xe), color='m', alpha=.8)
    tax.set_ylim(xe[x1:x2].min()*1.2,xe[x1:x2].max()*1.2)
    tax.set_ylabel('error', color='m')
    ax.legend(loc=2)

    fig.savefig('round_%s.png'%(rm))


