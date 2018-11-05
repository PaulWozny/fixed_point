
from random import uniform
from fixed_point import fixbv,W
import myhdl
from myhdl import bin


def test_basic():
    # Test all exact single bit values for W(16,0,15)
    for f in range(1,16):
        x = fixbv(2**-f, format=W(16,0,15))
        y = fixbv(-2**-f, format=W(16,0,15))
        print(f,x,y)
        assert float(x) == 2**-f, \
               "%s != %s, %04x != %04x" % (2.**-f, x,
                                           hex(x),
                                           hex(0x8000 >> f))
        
        assert bin(x,16) == bin(0x8000 >> f, 16), \
               "%s != %s for f == %d" % (bin(x, 16),
                                         bin(0x8000 >> f, 16), f)
        assert float(y) == -2**-f
        assert bin(y,16) == bin(-0x8000 >> f, 16), \
               "%s" % (bin(y, 16))

    # Test all exact single bit values for W128.0
    for f in range(1,128):
        x = fixbv(2**-f,  min=-1, max=1, res=2**-127)
        y = fixbv(-2**-f, min=-1, max=1, res=2**-127)
        assert float(x) == 2**-f
        assert bin(x,128) == bin(0x80000000000000000000000000000000 >> f, 128)
        assert float(y) == -2**-f
        assert bin(y,128) == bin(-0x80000000000000000000000000000000 >> f, 128)

    assert x > y
    assert y < x
    assert min(x,y) == min(y,x) == y
    assert max(x,y) == max(y,x) == x
    assert x != y

    x = fixbv(3.14159, format=W(18,3))
    y = fixbv(-1.4142 - 1.161802 - 2.71828, format=W(18,3))

    assert x != y
    #assert --x == x
    assert abs(y) > abs(x)
    assert abs(x) < abs(y)
    assert x == x and y == y

    # Create a W8.3 fixed-point object value == 2.5
    x = fixbv(2.5, min=-8, max=8, res=1./32)
    assert float(x) == 2.5
    assert int(x) == 0x50
    
    
def test_math():
    x = fixbv(0.5,  format=W(16,0))  
    y = fixbv(0.25, format=W(16,0))  
    z = fixbv(0, format=W(16,0))
    print(type(x), type(y), type(z))
    w = x + y
    print(w, type(w))
    z[:] = x + y
    print(z, type(z), x+y)
    assert float(z) == 0.75

    x = fixbv(3.5,   min=-8, max=8, res=2**-5)  
    y = fixbv(-5.25, min=-8, max=8, res=2**-5)
    iW = x.W + y.W
    print(iW)
    z = fixbv(0, format=iW)
    z[:] = x + y
    assert float(z) == -1.75

    x = fixbv(3.141592, format=W(19,4))  
    y = fixbv(1.618033, format=W(19,4))
    print(float(x), int(x), repr(x))
    print(float(y), int(y), repr(y))

    iW = x.W * y.W
    print(iW)
    z = fixbv(0, format=iW)
    wl,iwl,fwl = z.W.fmt
    print(repr(z), z._max, z._min, z._nrbits, "iwl, fwl", iwl, fwl)
    
    z[:] = x * y
    print(float(z), int(z), repr(z))
    assert z > 5.

    # @todo complex math calculation
    #for ii in range(5, 100):
    #    si = ii+1; sf = ii/5+2
    #    mi = si*2;   mf = sf*2
    #    sw = si + sf + 1
    #    mw = mi + mf + 1
    #    
    #    a  = fixbv(uniform(-1,1), format=W(sw,si))
    #    b  = fixbv(uniform(-1,1), format=W(sw,si))
    #    c  = fixbv(uniform(-1,1), format=W(mw,mi))
    #    
    #    d  = fixbv(uniform(-1,1), format=W(mw+1,mi+1))        
    #    ds = fixbv(uniform(-1,1), format=W(sw+1,si+1))
    #
    #    # @todo the result should be within some reasonable error
    #    #       add an assert that checks the error range.
    #    #       Currently it will simply accept not asserts/exceptions
    #    #       will occur.
    #    zz = ((a * b) - c ) >> 2
    #    #print "CM1 ", repr(zz), repr(a), repr(b), repr(c), repr(d)
    #
    #    zz = (a + b ) - ds
    #    #print "CM2 ", repr(zz), repr(a), repr(b), repr(c), repr(d)
    #
    #    zz = ((a*b) - c) * d
    #    #print "CM3 ", repr(zz), repr(a), repr(b), repr(c), repr(d)
    #
    #    zz = (a * b * c * d) << 4
    #    #print "CM4 ", repr(zz), repr(a), repr(b), repr(c), repr(d)
    #
    #    zz = ((a*b)>>8) + (c<<2) + d
    #    #print "CM5 ", repr(zz), repr(a), repr(b), repr(c), repr(d)

        
# example / test  from "main"
def test_create():
    """
    This test creates a bunch of different fixed-point objects.
    This test doesn't test correctness only test that creating and many
    of the public functions execute without error.
    """
    print("\n** Create W16.0 fxintbv")
    x = fixbv(0, min=-1, max=1, res=2**-15)
    print(x, hex(x), repr(x))

    print "\n** Create W9.3 fxintbv == 2.5"
    x = fixbv(2.5, min=-8, max=8, res=1./32)
    print(x, hex(x), repr(x))

    print("\n** Create W0.?? fxintbv == 0.0333")
    x = fixbv(0.0333, min=-1, max=1, res=0.0001)
    print(x, hex(x), repr(x))
    
    s = 0.5
    x = 0x4000
    for i in range(16):
        fxp = fixbv(s, min=-1, max=1, res=2**-15)
        s = s / 2
        print(str(fxp), myhdl.bin(fxp, 16), "%04x" % (fxp), type(fxp), repr(fxp))
        #print(hex(fxp & x)  @todo assert hex(fxp & x) == x, "Incorrect fixed-point calculation")
        x = x >> 1

    print("Get fixbv")
    a = fixbv(0, min=-2, max=2, res=2**-4)
    print("Assign to 1")
    a._val = 1
    print(a, repr(a))

    print("[1] Showing range: ")
    print("printing a:", a)
    print("slice operation (Note slice will return intbv)")
    print("  ", str(a), "  slice a[4:] ", hex(a[4:]), " a[16:] ", hex(a[16:]))

    a = fixbv(1.2, min=-2, max=2, res=2**-3)
    print("[2] Showing range: ")
    print("printing a: ", a)


    a = fixbv(0.02, min=-1, max=1, res=2**-8)
    print("[1] Representation a: ", repr(a))

    b = fixbv(0.2, min=-1, max=1, res=2**-8)
    print("[2] Representation b: ", repr(b))

    c = fixbv(0, format=a.W+b.W)
    print("[3] Representation c: ", c.W)

    print("[1] Add: c = a + b")
    c[:] = a + b
    print "c: ", c, type(c), repr(c)

    print("[2] Add: c = 1.25 + 2.0")
    a = fixbv(1.25, min=-4, max=4, res=2**-12)
    b = fixbv(2.0,  min=-4, max=4, res=2**-12)
    c = fixbv(0, format=a.W+b.W)
    print("  a: ", a.W, bin(a,len(a)), " b: ", b.W, bin(b,len(b)))
    c[:] = a + b
    print("c: ", c, c.W, bin(c,len(c)))



def test_round():
    pass


if __name__ == '__main__':
    test_basic()
    test_math()
    test_create()
