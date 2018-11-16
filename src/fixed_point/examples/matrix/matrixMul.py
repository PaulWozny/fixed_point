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

x1 = fixbv(0.54, min=-1, max=1, res=2**-10)
x2 = fixbv(0.22, min=-1, max=1, res=2**-15)

# The following works correctly:

print("Testing fixbv math operations for x1 = {0}, x2 = {1}".format(x1._fval, x2._fval))
print("x1 resolution = {0}, x2 resolution = {1}".format(x1.res, x2.res))

x_mul = x1 * x2
print("Result of multiplication: Value = {0}, Resolution = {1}".format(x_mul._fval, x_mul.res))

x_add = x1 + x2
print("Result of addition: Value = {0}, Resolution = {1}".format(x_add._fval, x_add.res))

x_sub = x1 - x2
print("Result of subtraction: Value = {0}, Resolution = {1}".format(x_sub._fval, x_sub.res))

