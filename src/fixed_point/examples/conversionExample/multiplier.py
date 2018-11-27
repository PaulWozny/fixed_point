from myhdl import *


@block
def multply(A,B, output_mul):
    """

    :param A:
    :param B:
    :param output_mul:
    :return:
    """

    @always_comb
    def mulll():

        output_mul = A * B

    return mulll
