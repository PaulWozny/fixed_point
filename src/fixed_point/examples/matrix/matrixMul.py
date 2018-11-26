#

'''
Functions for matrix multiplication.

'''

from fixed_point import fixbv, fixed
from myhdl import intbv, bin
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

x1 = fixbv ( 0.54, min=-1, max=1, res=2 ** -10 )
x2 = fixbv ( 0.22, min=-1, max=1, res=2 ** -15 )

# The following works correctly:

print ( "Testing fixbv math operations for x1 = {0}, x2 = {1}".format ( x1._fval, x2._fval ) )
print ( "x1 resolution = {0}, x2 resolution = {1}".format ( x1.res, x2.res ) )

x_mul = x1 * x2
print ( "Result of multiplication: Value = {0}, Resolution = {1}".format ( x_mul._fval, x_mul.res ) )
print ( x_mul )
x_add = x1 + x2
print ( "Result of addition: Value = {0}, Resolution = {1}".format ( x_add._fval, x_add.res ) )
print ( x_add )
x_sub = x1 - x2
print ( "Result of subtraction: Value = {0}, Resolution = {1}".format ( x_sub._fval, x_sub.res ) )

# Multiplication of 4x4 matrices using fixed_point
q1 = fixbv ( 0.44, min=-1, max=1, res=2 ** -15 )
q2 = fixbv ( 0.32, min=-1, max=1, res=2 ** -15 )
q3 = fixbv ( 0.19, min=-1, max=1, res=2 ** -15 )
q4 = fixbv ( 0.37, min=-1, max=1, res=2 ** -15 )

y1 = fixbv ( 0.20, min=-1, max=1, res=2 ** -15 )
y2 = fixbv ( 0.12, min=-1, max=1, res=2 ** -15 )
y3 = fixbv ( 0.15, min=-1, max=1, res=2 ** -15 )
y4 = fixbv ( 0.32, min=-1, max=1, res=2 ** -15 )

# c00 = a[0][0]*b[0][0]+a[0][1]*b[1][0]
# print(c00)
# c01 = a[0][0]*b[0][1]+a[0][1]*b[1][1]
# print(c01)
# c10 = a[1][0]*b[0][0]+a[1][1]*b[1][0]
# print(c10)
# c11 = a[1][0]*b[0][1]+a[1][1]*b[1][1]
# print(c11)

# Fixed matrix multiplication


# result = numpy.zeros ( [ 2, 2 ], dtype=fixbv )
# print(result[0][0])

# a = numpy.array ([ [ q1, q2 ],
#                    [ q3, q4 ] ], dtype=fixbv)
# b = numpy.array ([ [ y1, y2 ],
#                    [ y3, y4 ] ], dtype=fixbv)
#
# c = numpy.array ([ [ c1, c2 ],
#                    [ c3, c4 ] ], dtype=fixbv)

a = list ( [ [ q1, q2 ], [ q3, q4 ] ] )
b = list ( [ [ y1, y2 ], [ y3, y4 ] ] )
# print(c)

def matrixmultiplication(a, b):


    c1 = fixbv ( 0, min=-2, max=2, res=2 ** -15 )
    c2 = fixbv ( 0, min=-2, max=2, res=2 ** -15 )
    c3 = fixbv ( 0, min=-2, max=2, res=2 ** -15 )
    c4 = fixbv ( 0, min=-2, max=2, res=2 ** -15 )
    result = list ( [ [ c1, c2 ],
                      [ c3, c4 ] ] )

    for i in range ( len ( a ) ):

        #print ( "iteration of columns a", i )
        for j in range ( len ( b[ 0 ] ) ):
            #print ( "iteration of rows b[0]", j )
            for k in range ( len ( b ) ):
                #print ( "iteration of row b", k )
                #print ( "listof", result[ i ][ j ] )
                result[ i ][ j ] += a[ i ][ k ] * b[ k ][ j ]
    print("Result of matrixmultiplication", result)
    for r in result:

        # print ( "Result of matrixmultiplication: Value = {0}, Resolution = {1}".format ( r[0]._fval, r[0].res ) )
        # print ( "Result of matrixmultiplication: Value = {0}, Resolution = {1}".format ( r[ 1 ]._fval, r[ 1 ].res ) )
        #print ( "Matrix multiplication", format (r) )

        print("Matrix multiplication fval", r[0]._fval, r[1]._fval)
    return;


matrixmultiplication ( a, b );

c000 = fixbv ( 0, min=-2, max=2, res=2 ** -15 )
c001 = fixbv ( 0, min=-2, max=2, res=2 ** -15 )

c000[ : ] = q1 * y1
c001 = q2 * y3
# print("original", q1._fval)
# print(len(q1))
# print("from array", a[0][0])
# print(format(c00))
# print("bin mult ")
# print("Result of multiplication: Value = {0}, Resolution = {1}".format(c000._fval, c000.res))
# print(c001._fval)
cp = fixbv ( 0, min=-2, max=2, res=2 ** -15 )
cp[ : ] = c000 + c001
# print(cp)
# print(cp._fval)
print ( "Result of addition and multiplication for cp00: Value = {0}, Resolution = {1}".format ( cp, cp.res ) )
