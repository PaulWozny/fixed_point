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

# Multiplication of 4x4 matrices using fixed_point
q1 = fixbv(0.44, min=-1, max=1, res=2**-15)
q2 = fixbv(0.22, min=-1, max=1, res=2**-15)
q3 = fixbv(0.19, min=-1, max=1, res=2**-15)
q4 = fixbv(0.37, min=-1, max=1, res=2**-15)

y1 = fixbv(0.20, min=-1, max=1, res=2**-15)
y2 = fixbv(0.12, min=-1, max=1, res=2**-15)
y3 = fixbv(0.15, min=-1, max=1, res=2**-15)
y4 = fixbv(0.32, min=-1, max=1, res=2**-15)

#a =[[q1._fval, q2._fval], [q3._fval, q4._fval]]
# b =[[y1._fval, y2._fval], [y3._fval, y4._fval]]

#a =[[q1, q2], [q3, q4]]
#b =[[y1, y2], [y3, y4]]




#a =[[1, 2], [3, 4]]
#b =[[1, 2], [3, 4]]

#result =[[0, 0], [0, 0]]
#print (numpy.matmul(a,b))


# ress = fixbv(0, min=-1, max=1, res=2**-15)

# result=[[ress._fval, ress._fval], [ress._fval, ress._fval]]
# result=[[ress, ress], [ress, ress]]






# c00 = a[0][0]*b[0][0]+a[0][1]*b[1][0]
# print(c00)
# c01 = a[0][0]*b[0][1]+a[0][1]*b[1][1]
# print(c01)
# c10 = a[1][0]*b[0][0]+a[1][1]*b[1][0]
# print(c10)
# c11 = a[1][0]*b[0][1]+a[1][1]*b[1][1]
# print(c11)
# print(c11._fval)


#Fixed matrix multiplication
# a = [[q1, q2],
#      [q3, q4]]
# b = [[y1, y2],
#      [y3, y4]]
result = numpy.zeros([2, 2], dtype=fixbv)
a = numpy.array([[q1, q2], [q3, q4]], dtype=fixbv)
b = numpy.array([[y1, y2], [y3, y4]], dtype=fixbv)

c00 = (a[0][0] * b[0][0])#+ (a[0][1] * b[1][0])
#print(c00)
c01 = a[0][0] * b[0][1] + a[0][1] * b[1][1]
#print(c01)
c10 = a[1][0] * b[0][0] + a[1][1] * b[1][0]
#print(c10)
c11 = a[1][0] * b[0][1] + a[1][1] * b[1][1]
#print(c11)

c22 = [c00, c01, c10, c11]
# c23 = bytearray

print(c00, c01)
print(c10, c11)
#print(c22[0])

# a = numpy.array([[q1, q2], [q3, q4]], dtype=fixbv)
# b = numpy.array([[y1, y2], [y3, y4]], dtype=fixbv)


print(a[0][0])
print(b[0][0])
c= a*b
print(c)

#print(a*b)

for i in range(len(a)):
   # iterate through columns of Y
   for j in range(len(b[0])):
       # iterate through rows of Y
       for k in range(len(b)):
           result[i][j] += a[i][k] * b[k][j]
for r in result:
   print(r)
