from adder import adder
from multiplier import multply
from fixed_point import fixbv
from myhdl import *


def alu_tb():


    clk = Signal(0)


    x1 = Signal(fixbv(0.5, min=-2, max=2, res=2**-15))
    x2 = Signal(fixbv(0.5, min=-2, max=2, res=2**-15))
    output_add = Signal(fixbv(0, min=-2, max=4, res=2**-15))
    output_mul = Signal(fixbv(0, min=-2, max=4, res=2 ** -15))

    add = adder(x1, x2, output_add)

    mul = multply(x1, x2, output_mul)

    return add, mul



# inst = alu_tb()
# inst.run_sim(50)
twoja = alu_tb()
twoja.convert(hdl='VHDL')



# x1 = Signal(fixbv(1.5, min=-2, max=2, res=2**-15))
# x2 = Signal(fixbv(0.25, min=-2, max=2, res=2**-10))
# out = Signal(fixbv(0, min=-4, max=4, res=2**-20))
# out=x1+x2
# print(out)
# print(out._val)
# print(out.res)

# x1 = Signal(fixbv(0, min=0, max=2, res=2**-15))
# x2 = Signal(fixbv(0.25, min=0, max=2, res=2**-10))
# output = Signal(fixbv(0, min=-4, max=4, res=2**-20))

#
# add = adder(x1, x2, output)
#
# x1 = Signal(fixbv(1.5, min=-2, max=2, res=2**-15))
#
# print(output)
#
