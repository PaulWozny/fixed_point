"""
This is an example applying the fixed point data types.  This example
is based off the example in Randy Yates \"Fixed-Point Arthimetic :
An Introduction\" article.

:Author: Christopher Felton
"""
import argparse
from math import log, ceil, floor

from numpy.random import uniform

from myhdl import *
from myhdl_tools import Clock,Reset
from fixed_point import fixed,fixbv


def sos(x):
    y = 0;
    for ii in range(len(x)):
        y += x[ii]**2

    return y

def sum_of_squares(clock, reset, x, y, N=16):
    """
    @type 
    @param     
    """

    buf = [Signal(0.) for ii in range(N)]
    ii  = Signal(0)
    
    @always_seq(clock.posedge, reset=rest)
    def g_sosw():
        buf[int(ii)].next = x
        ii.next = (ii + 1) % N
        
        y.next = sos(buf) / float(N)
            
    return g_sosw


def m_sum_of_squares(clock, reset, x, y, N=16):
    """
    This module is the fixbv type
    """
    assert isinstance(x, fixbv)
    assert isinstance(y, fixbv)
    smin,smax,sres = (x.min**2,xmax**2,x.res**2)
    buf = [Signal(fixbv(0, xmin, xmax, xres)) for i in range(N)]
    sqr = [Signal(fixbv(0, smin, smax, sres)) for i in range(N)]

    # Check that N is a power of 2
    ii   = Signal(modbv(0, min=0, max=N))
    
    @always_seq(clock.posedge, reset=reset)
    def rtl_input():
        buf[int(ii)].next = x
        ii.next = ii + 1
                
    @always_comb
    def rtl_square():
        for jj in range(N):
            sqr[jj].next = buf[jj] * buf[jj]

    xsum = fixbv(0, smin*N, smax*N, sres)
        
    # Currently N is limited to a power of two
    divn = int(log(N,2))
    @always_seq(clock.posedge, reset=reset)
    def rtl_sum():
        xsum[:] = sqr[0]
        for jj in range(1,N):
            xsum[:] = xsum + sqr[jj].val

        y.next = xsum >> divn

                
    return instances()


def testbench(args):
    """
    """

    run = args.simtype
    N = args.N
    Nloops = args.NLoops
    
    clock = Signal(bool(0))
    reset = ResetSignal(0, active=0, async=True)
    xfp = Signal(0.0)
    yfp = Signal(0.0)

    xfx = Signal(fixbv(0, min=-1, max=1, res=2**-15))
    yfx = Signal(fixbv(0, min=-1, max=1, res=2**-30))

    print repr(xfx), repr(yfx)
    tb_dut_fp = sum_of_squares(clk, rst, xfp, yfp, N)
    if run == "trace":
        tb_dut_fx = traceSignals(m_sum_of_squares, clock, reset, xfx, yfx, N)
    else:
        tb_dut_fx = m_sum_of_squares(clock, reset, xfx, yfx, N)

    @always(delay(3))
    def tb_clock():
        clock.next = not clock

    @always(clock.posedge)
    def tb_init():
        f = .9999 #uniform(-1,1)
        xfp.next = f
        xfx.next = xfx.Round(f)

    @instance
    def stimulus():
        yield clk.posedge
        rst.next = True
        yield delay(10)
        rst.next = False
        yield delay(1)

        for ii in range(Nloops): # 
            for jj in range(N):
                yield clk.posedge
                print " FP: %-03.6f [%-03.6f], FX: %-03.6f [%-03.6f] ( %08x, %08x)" % \
                      (yfp, xfp, yfx.fValue, xfx.fValue, yfx, xfx)
                print "Error Squared %f" % ((yfp - yfx.fValue)**2)
        raise StopSimulation
    

    Simulation((tb_clock, tb_init, tb_stim, tb_dut_fp, tb_dut_fx)).run()

def _create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--simtype', type=str, default='run', choices=('run','trace'),
                        help='')
    parser.add_argument('--N', type=int, default=16,
                        help='')
    parser.add_argument('--NLoops', type=int, default=4)
    return parser
                       
if __name__ == "__main__":
    parser = _create_parser()
    args = parser.parse_args()
    testbench(args)
