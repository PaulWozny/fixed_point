from fixed_point import fixbv
import random

# Testbench for checking math operations (mul, add, sub) on fixbv objects
# Parameters:
#   loops       = number of iterations to check
#   minmaxPower = maximum power for bounds    (2^minmaxPower)
#   resPower    = maximum power of resolution (2^resPower)

loops = 5000
resPower = 32
minmaxPower = 20

for x in range (0, loops):
    # Generate random fixbv object named x1
    x1_res_power = random.randint(1, resPower)
    x1_res = 2**-x1_res_power
    x1_min = random.randint(-2**minmaxPower, 0)
    x1_max = random.randint(0, 2**minmaxPower)
    x1_val = random.uniform(x1_min, x1_max)
    x1 = fixbv(x1_val, min=x1_min, max=x1_max, res=x1_res)

    # Generate random fixbv object named x2
    x2_res_power = random.randint(1, resPower)
    x2_res = 2**-x2_res_power
    x2_min = random.randint(-2**minmaxPower, 0)
    x2_max = random.randint(0, 2**minmaxPower)
    x2_val = random.uniform(x2_min, x2_max)
    x2 = fixbv(x2_val, min=x2_min, max=x2_max, res=x2_res)

    # Math operations on fixbv objects
    x_mul = x1 * x2
    x_add = x1 + x2
    x_sub = x1 - x2

    # Math on regular numbers (the values input to fixbv contructors)
    x_mul_chk = x1_val * x2_val
    x_add_chk = x1_val + x2_val
    x_sub_chk = x1_val - x2_val

    # Calculating errors and max errors for operations

    # For multiplication it comes from:
    # (x1_fval + x1_err)*(x2_fval + x2_err) - x1_fval*x2_fval
    # where max values of x1_err = x1_res; x2_err = x2_res
    # absolute values of everything because we could multiply a positive number by a negative
    mul_err = abs(x_mul.get_float - x_mul_chk)
    mul_maxerr = abs(x1.get_float * x2.res) + abs(x2.get_float * x1.res) + abs(x1.res * x2.res)

    # Max error for addition is the sum of resolutions
    add_err = abs(x_add.get_float - x_add_chk)
    add_maxerr = abs(x1_res + x2_res)

    # Max error for subtraction is the sum of resolutions
    sub_err = abs(x_sub.get_float - x_sub_chk)
    sub_maxerr = abs(x1_res + x2_res)

    # Check for a larger error in multiplcation
    if mul_err >= mul_maxerr:
        print("Multiplication error: {0} >= {1}".format(mul_err, mul_maxerr))
        print("x1: Value = {0}, Resolution = {1}".format(x1.get_float, x1.res))
        print("x2: Value = {0}, Resolution = {1}".format(x2.get_float, x2.res))
        print("x1_val = {0}, x2_val = {1}".format(x1_val, x2_val))
        print("x_mul = {0}, x_mul_chk = {1}".format(x_mul.get_float, x_mul_chk))

    # Check for a larger error in addition
    if add_err >= add_maxerr:
        print("Addition error: {0} >= {1}".format(add_err, add_maxerr))
        print("x1: Value = {0}, Resolution = {1}".format(x1.get_float, x1.res))
        print("x2: Value = {0}, Resolution = {1}".format(x2.get_float, x2.res))
        print("x1_val = {0}, x2_val = {1}".format(x1_val, x2_val))
        print("x_add = {0}, x_add_chk = {1}".format(x_add.get_float, x_add_chk))

    # Check for a larger error in subtraction
    if sub_err >= sub_maxerr:
        print("Subtraction error: {0} >= {1}".format(sub_err, sub_maxerr))
        print("x1: Value = {0}, Resolution = {1}".format(x1.get_float, x1.res))
        print("x2: Value = {0}, Resolution = {1}".format(x2.get_float, x2.res))
        print("x1_val = {0}, x2_val = {1}".format(x1_val, x2_val))
        print("x_sub = {0}, x_sub_chk = {1}".format(x_sub.get_float, x_sub_chk))
