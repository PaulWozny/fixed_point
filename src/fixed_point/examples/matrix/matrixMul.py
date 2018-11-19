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

# print("Testing fixbv math operations for x1 = {0}, x2 = {1}".format(x1._fval, x2._fval))
# print("x1 resolution = {0}, x2 resolution = {1}".format(x1.res, x2.res))
#
# x_mul = x1 * x2
# print("Result of multiplication: Value = {0}, Resolution = {1}".format(x_mul._fval, x_mul.res))
#
# x_add = x1 + x2
# print("Result of addition: Value = {0}, Resolution = {1}".format(x_add._fval, x_add.res))
#
# x_sub = x1 - x2
# print("Result of subtraction: Value = {0}, Resolution = {1}".format(x_sub._fval, x_sub.res))

# Multiplication of 4x4 matrices using fixed_point
q1 = fixbv(0.44, min=-1, max=1, res=2**-15)
q2 = fixbv(0.22, min=-1, max=1, res=2**-15)
q3 = fixbv(0.19, min=-1, max=1, res=2**-15)
q4 = fixbv(0.37, min=-1, max=1, res=2**-15)

y1 = fixbv(0.20, min=-1, max=1, res=2**-15)
y2 = fixbv(0.12, min=-1, max=1, res=2**-15)
y3 = fixbv(0.15, min=-1, max=1, res=2**-15)
y4 = fixbv(0.32, min=-1, max=1, res=2**-15)

# a =[[q1._fval, q2._fval], [q3._fval, q4._fval]]
# b =[[y1._fval, y2._fval], [y3._fval, y4._fval]]

a =[[q1, q2], [q3, q4]]
b =[[y1, y2], [y3, y4]]

# print (a[0][0]*b[0][0])
# c = q1*y1
# print (c)
# c = c*c
# print(c)


# d = [[a[0][0]*b[0][0]+a[0][1]*b[1][0]]]
d = a[0][0]*b[0][0]
print (d)
d = [a[0][0]*b[0][0]]
print (d)
print (d[0])
# print (d)

d[0]= [a[0][0]*b[0][0]]
print (d)
# print (d[0])
# print (d)



# C = C*C
# # C = [[a[0][0]*b[0][0]+a[0][1]*b[1][0]]]
# print (C)


def fixed4x4MatrixMul(A,B):

    C = [[A[0][0]*B[0][0]+A[0][1]*B[1][0]]]
    return C[0]


print(fixed4x4MatrixMul(a,b))









#a =[[1, 2], [3, 4]]
#b =[[1, 2], [3, 4]]

#result =[[0, 0], [0, 0]]
#print (numpy.matmul(a,b))


# ress = fixbv(0, min=-1, max=1, res=2**-15)

# result=[[ress._fval, ress._fval], [ress._fval, ress._fval]]
# result=[[ress, ress], [ress, ress]]

#
#
# for i in range(len(a)):
#    # iterate through columns of Y
#    for j in range(len(b[0])):
#        # iterate through rows of Y
#        for k in range(len(b)):
#            result[i][j] += a[i][k] * b[k][j]
# print(result)
# for r in result:
#    print(r)