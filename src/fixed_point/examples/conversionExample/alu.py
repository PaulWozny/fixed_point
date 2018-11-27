from myhdl import *
from fixed_point import *


@block
def adderClk(A, B, output2):
    """

    :param A:  input
    :param B: input
    :param output2: output
    :return:
    """

    clk = Signal(0)
    @always(delay(10))
    def drive_clk():
        clk.next = not clk

    @always(clk.posedge)
    # @always_comb
    def seq():
        print(A)
        print(B)
        sum = A + B
        print(sum)
        # retVal = fixbv(sum._fval, format=sum._W)
        retVal = sum
        output2.next = retVal
        print(output2)

    return drive_clk, seq

# @block
# def adder(A, B, output2):
#     """
#
#     :param A:  input
#     :param B: input
#     :param output2: output
#     :return:
#     """
#
#
#     @always_comb
#     def seq():
#         output2.next = A + B
#
#     return seq


