from myhdl import *
from fixed_point import *


@block
def adder(A,B, output2, clk, reset):
    """

    :param A:  input
    :param B: input
    :param output2: output
    :param clk:
    :param reset:
    :return:
    """

    @always_seq(clk.posedge, reset=reset)
    def seq():
        output2.next = A+B

    return seq



