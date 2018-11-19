from  myhdl import Signal, intbv, conversion, ResetSignal
from alu import adder
from fixed_point import fixbv

def adder_tb():

    # x1 = fixbv(0.22, min=-1, max=1, res=2**-15) # this is bad
    # x2 = fixbv(0.22, min=-1, max=1, res=2**-15)
    # output = fixbv(0.22, min=-1, max=1, res=2**-15)

    x1 = Signal(fixbv(0.22, min=-1, max=1, res=2**-15))
    x2 = Signal(fixbv(0.22, min=-1, max=1, res=2**-15))
    output = Signal(fixbv(0, min=-1, max=1, res=2**-15))



    print(hex(x1))
    print(hex(x1 + x2))
    # x1 = intbv(32, min=-1000, max=10000)
    # x2 = intbv(22, min=-1000, max=10000)
    # output = intbv(0, min=-1000, max=10000)

    # x1 = Signal(intbv(32, min=-1000, max=10000))
    # x2 = Signal(intbv(22, min=-1000, max=10000))
    # output = Signal(intbv(0, min=-1000, max=10000))

    clk = Signal(bool(0))
    reset= ResetSignal(0, active=0, async=True)
    add = adder(x1, x2, output, clk, reset)

    add.convert(hdl='VHDL')
    add.convert(hdl='Verilog')

    output.read

adder_tb()

# print(output.read)