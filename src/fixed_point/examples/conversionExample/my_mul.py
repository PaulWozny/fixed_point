from myhdl import *
from fixed_point import *

@block
def my_mul(a, b, c):
    @always_comb
    def logic():
        c.next = a * b
    return logic


@block
def my_tb():
    a = Signal(fixbv(0.5, min=-1, max=1, res=2**-9))
    b = Signal(fixbv(0.25, min=-2, max=2, res=2**-10))
    c = Signal(fixbv(0, min=-1, max=1, res=2**-20))

    @instance
    def stim():
        yield delay(10)
        a.next = 3
        b.next = 4
        yield delay(10)
        raise StopSimulation()

    uut = my_mul(a, b, c)
    uut.convert(hdl='VHDL')

    return instances()

tb = my_tb()
tb.config_sim(trace=True)
tb.run_sim()