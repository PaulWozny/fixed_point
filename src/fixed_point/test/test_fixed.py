
from random import uniform
from fixed_point import fixed,W
import myhdl
from myhdl import bin

def _round_modes1(ival,tdict):
     for rm,rval in tdict.items():
        print('  rnd[%10s]: %f'%(rm,ival))
        x = fixed(ival, min=-2,max=2, res=.5, round_mode=rm)
        assert float(x) == rval, "%s expected %f got %f"%(rm,rval,float(x))
        
def test_round():
    """
       round modes
       -----------
          ceil       : always round up
          fix        : always towards zero
          floor      : truncate, awlays round down
          nearest    : tie, towards largest absolute value
          round      : tie, to +infinity
          convergent : tie to closest even (round_even)
    """

    # considering binary rounding with decimal numbers
    # can be tricky (at least for me).  In the following
    # the resolution is .5.  That means, the valid numbers
    # are -.5,0,.5,1 ... .  Halfway between adjacent numbers
    # is x+.25.  Example, .5 halfway is .75, normal rounding
    # everything between .5 to .75 is rounded to .5 and
    # every .75 to 1 is rounded to 1.  In this resolution
    # even numbers are whole numbers (1,0,-1) odd numbers
    # are the fraction (1.5,.5,-.5)
    
    # the valid results should be 1,.5
    ival = .54
    tdict = {'ceil':1, 'fix':.5, 'floor':.5, 'nearest':.5,
             'round':.5, 'convergent':.5}
    _round_modes1(ival,tdict)

    # the valid results should be 1,.5
    ival = .55
    tdict = {'ceil':1, 'fix':.5, 'floor':.5, 'nearest':.5,
             'round':.5, 'convergent':.5}
    _round_modes1(ival,tdict)

    # the valid results should be 1,.5
    ival = .75
    tdict = {'ceil':1, 'fix':.5, 'floor':.5, 'nearest':1,
             'round':1, 'convergent':1}
    _round_modes1(ival,tdict)

    ival = .76
    tdict = {'ceil':1, 'fix':.5, 'floor':.5, 'nearest':1,
             'round':1, 'convergent':1}
    _round_modes1(ival,tdict)



    ival = -.54
    tdict = {'ceil':-.5, 'fix':-.5, 'floor':-1, 'nearest':-.5,
             'round':-.5, 'convergent':-.5}
    _round_modes1(ival,tdict)

    # the valid results should be 1,.5
    ival = -.75
    tdict = {'ceil':-.5, 'fix':-.5, 'floor':-1, 'nearest':-1,
             'round':-1, 'convergent':-1}
    _round_modes1(ival,tdict)

    ival = -.76
    tdict = {'ceil':-.5, 'fix':-.5, 'floor':-1, 'nearest':-1,
             'round':-1, 'convergent':-1}
    _round_modes1(ival,tdict)


    
def test_basic():
    # Test all exact single bit values for W(16,0,15)
    for f in range(1,16):
        x = fixed(2**-f, format=W(16,0,15))
        y = fixed(-2**-f, format=W(16,0,15))
        #print(f,x,y)
        assert float(x) == 2**-f, \
               "%f != %f" % (float(x),2**-f)
        assert bin(x,16) == bin(0x8000>>f,16), \
               "%s != %s for f == %d" % (bin(x, 16),
                                         bin(0x8000 >> f, 16), f)
        assert float(y) == -2**-f, \
               "%f != %f" % (float(x),2**-f)
        assert bin(y,16) == bin(-0x8000 >> f, 16), \
               "%s" % (bin(y, 16))


    # Test all exact single bit values for W128.0
    for f in range(1,128):
        x = fixed(2**-f,  min=-1, max=1, res=2**-127)
        y = fixed(-2**-f, min=-1, max=1, res=2**-127)
        assert float(x) == 2**-f
        assert bin(x,128) == bin(0x80000000000000000000000000000000 >> f, 128)
        assert float(y) == -2**-f
        assert bin(y,128) == bin(-0x80000000000000000000000000000000 >> f, 128)

    assert x > y
    assert y < x
    assert min(x,y) == min(y,x) == y
    assert max(x,y) == max(y,x) == x
    assert x != y

    x = fixed(3.14159, format=W(18,3))
    y = fixed(-1.4142 - 1.161802 - 2.71828, format=W(18,3))

    assert x != y
    #assert --x == x
    assert abs(y) > abs(x)
    assert abs(x) < abs(y)
    assert x == x and y == y

    # Create a W8.3 fixed-point object value == 2.5
    x = fixed(2.5, min=-8, max=8, res=1./32)
    assert float(x) == 2.5
    assert int(x) == 0x50    


def test_math():
    x = fixed(0.5, format=W(16,0))
    y = fixed(0.25, format=W(16,0))
    w = x + y       # typical modeling
    print(repr(w),repr(x),repr(y))

    # pre-declared
    z = fixed(0, format=x+y)
    z[:] = x + y    # hardware transfer (type is declared)
    print(repr(z),repr(x),repr(y))
    
    assert float(w) == 0.75
    assert float(z) == 0.75

    # test non-aligned additions
    x = fixed(0.5, min=-4, max=4, res=.125)
    y = fixed(0.25, min=-16, max=16, res=.0625)
    print(repr(z),repr(x),repr(y))    
    z = x+y
    print(repr(z),repr(x),repr(y))
    assert float(z) == 0.75

    # test non-aligned additions and overflow
    x = fixed(0.5, min=-4, max=4, res=2**-32)
    y = fixed(1.5, min=-16, max=16, res=2**-32)
    z = x+y
    print(repr(z),repr(x),repr(y))
    assert float(z) == 2.0

    # @todo: negative iwl and fwl

    # test subtraction
    x = fixed(0.5, format=W(16,0))
    y = fixed(0.25, format=W(16,0))
    z = x - y  
    print('S',repr(z),repr(x),repr(y))
    assert float(z) == 0.25

    x = fixed(0.5, min=-4, max=4, res=.125)
    y = fixed(0.25, min=-16, max=16, res=.0625)
    z = x-y
    print('S',repr(z),repr(x),repr(y))
    assert float(z) == 0.25

    z = y-x
    print('S',repr(z),repr(x),repr(y))
    assert float(z) == -0.25

    x = fixed(10.33, min=-16, max=16, res=.125)
    y = fixed(10.33, min=-16, max=16, res=.125)
    z = x-y
    print('S',repr(z),repr(x),repr(y))
    assert float(z) == 0.

    # The resolution of x is .125, it means 0.33 will be
    # rounded to .25 or .375 (it should be .375).  For
    # y the resolution is 2**-8 and the actual value should
    # be .328125 or .33203125 (.32 is closer?)
    x = fixed(0.33, min=-1, max=1, res=.125) 
    y = fixed(0.33, min=-1, max=1, res=2**-8)
    z = x+y
    print('A',repr(z),repr(x),repr(y))
    assert float(z) == 0.375+0.328125

    x = fixed(0.33, min=-1, max=1, res=.125)
    y = fixed(0.33, min=-1, max=1, res=2**-8)
    z = x-y
    print('S',repr(z),repr(x),repr(y))
    assert float(z) == 0.375-0.328125

    
    x = fixed(-1, format=W(8,0,7)) + .5
    assert float(x) == -.5



if __name__ == '__main__':
    test_round()
    #test_basic()
    #test_math()
