from myhdl import *
from fixed_point import *


@block
def adder(A, B, output_add):
    """

    :param A:  input
    :param B: input
    :param output2: output
    :return:
    """

    # @always(clk.posedge)
    @always_comb
    def adddd():
        print(A)
        print(B)
        sum = A + B
        print(sum)
        # retVal = fixbv(sum._fval, format=sum._W)
        retVal = sum
        output_add.next = retVal
        print(output_add)
    return adddd

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


