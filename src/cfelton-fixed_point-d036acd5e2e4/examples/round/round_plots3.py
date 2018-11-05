
import numpy as np
import matplotlib.pyplot as plt

from fixed_point import fixed,W
from fixed_point import ROUND_MODES

format1 = W(7,3,3)
format2 = W(4,3,0)
for rm in ROUND_MODES:
    xf = np.arange(-10000,10000)/1000.
    xq1,xq2,xe = ([],[],[])
    for ff in xf:
        fx1 = float(fixed(ff, format=format1, round_mode=rm))
        fx2 = float(fixed(fx1, format=format2, round_mode=rm))
        xq1.append(fx1)
        xq2.append(fx2)
        xe.append(fx1-fx2) # also plot error

    # plot the quantized values
    fig,ax = plt.subplots(1)
    tax = ax.twinx()
    ax.plot(xf,xf, label='real number')
    ax.plot(xf,xq1, label='quantized W(7,3,3)')
    ax.plot(xf,xq2, label='quantized W(7,3,3) -> W(4,3,0)')
    ax.grid(True)
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_title("Quantization\nfixed(format=(4,0,3),"
              "round_mode='%s'"
              "overflow_mode='saturate')"%(rm))
    ax.set_ylabel('Output (quantized)')
    ax.set_xlabel('Input')

    tax.plot(xf,xe, 'm:', alpha=.7, label='error')    
    xf = np.array(xf)
    x1,x2 = (xf == -7).nonzero()[0][0],(xf == 7).nonzero()[0][0]
    xe = np.array(xe)
    tax.axhline(np.mean(xe[x1:x2]), 0, len(xe), color='m', alpha=.8)
    tax.set_ylim(xe[x1:x2].min()*1.6,xe[x1:x2].max()*1.6)
    tax.set_ylabel('error', color='m')
    ax.legend(loc=2)

    sfmt = repr(format2).replace('[', '')
    sfmt = sfmt.replace(']', '')
    sfmt = sfmt.replace('(', '_')
    sfmt = sfmt.replace(')', '')
    sfmt = sfmt.replace(',','_')
    fig.savefig('plots/round_plot3_%s_%s.png'%(rm,sfmt))


