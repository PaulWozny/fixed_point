#

'''
Functions for matrix multiplication.

'''

from fixed_point import fixbv, fixed
from myhdl import intbv
import numpy

# class fixmul()

# def fixmul(A, B)
    # "Fixed point multipilation."

# 1 - Simple example

# fixNum1 = fixed(0.257, min=-1, max=1, res=2**-15)
# print(fixNum)
#
# # fixNum2 = fixed(value=0.257)
# print(fixNum * fixNum)

# retval = fixbv(0, min=-1, max=1, res=2**-31)
# retval3 = intbv(12)

# fixNum * retval3
# print((retval))
# print(retval._fval)


# A = [[fixNum, fixNum], [fixNum, fixNum]]
# B = [[fixNum, fixNum], [fixNum, fixNum]]
# C = numpy.matmul(A,B)

# ---

x1 = fixbv(0.54, min=-1, max=1, res=2**-15)
x2 = fixbv(0.22, min=-1, max=1, res=2**-15)
print(hex(x1), hex(x2))

# following expression yelds wrong result
# it multiplies two numbers (0x451E * 0x1C28
# which is equal to 79A14B0 ( 127538352 )
print(float(x1 * x2))
