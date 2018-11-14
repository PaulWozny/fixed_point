**************************
MyHDL Fixed-Point Package
**************************

This package is a work in progress and has **not** reach a stable 
release point, use at your own risk.  
 
This package adds fixed-point support to MyHDL.  The package intent is to 
provide a flexible approach to modeling and converting fixed-point data
types.

I provide a brief introduction to fixed-point 
`in this blog post <http://www.dsprelated.com/showarticle/139.php>`_.

The fixed_point package provides two different fixed-point types,
*fixed* and *fixbv*.  The *fixed* type is a higher level type 
and useful for modeling only.  The *fixed* object will automatically 
grow and align as needed.  The *fixed* can be resized by simply 
creating a new *fixed* (see example below).

There are two methods for creating a fixed-point (fixed,fixbv) by
specifing the minimum, maximum, and resolution properities or by
defining the format.  The fixed-point parameters are:

    * min : minimum value
    * max : the maximum value
    * res : minimum fractional step
    * format : The *W* format W(width, integer-width, fractional-width)

The min,max,res or the format is specified **not** both.

.. There are two methods for creating a fixed-point (fixed,fixbv) by
.. specifing the minimum, maximum, and resolution properities or by
.. defining the format.  The properties are 


--------------------
Examples of Usage
--------------------

Example using the *fixed* type.

    >>> x1 = fixed(0, min=-1, max=1, res=2**-3)
    >>> x2 = fixed(0, min=-1, max=1, res=2**-3)
    >>> x3 = x1 + x2
    # resize x2 to W(4,0,3)
    >>> x3 = fixed(x3, min=-1, max=1, res=2**-3, round_mode='fix')
    # or x3 = fixed(x3, format=W(4,0,3), round_mode='fix')


The following is an illustration how to plot the quantization
for a W(4,0,3) format:

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> 
    >>> from fixed_point import fixed
    >>> from fixed_point import ROUND_MODES
    >>> 
    >>> 
    >>> for rm in ROUND_MODES:
    >>>     xf = np.arange(-1200,1200)/1000.
    >>>     xq,xe = ([],[])
    >>>     for ff in xf:
    >>>         fx = float(fixed(ff, format=(4,0,3), round_mode=rm))
    >>>         xq.append(fx)    # back to float for plotting, preserves value
    >>>         xe.append(ff-fx) # also plot error


   * `ceil round`_
   * `floor round`_
   * `fix round`_
   * `nearest round`_
   * `round`_
   * `convergent round`_

.. _ceil round : https://bitbucket.org/cfelton/fixed_point/raw/tip/examples/round/round_ceil.png
.. _floor round : https://bitbucket.org/cfelton/fixed_point/raw/tip/examples/round/round_floor.png
.. _fix round : https://bitbucket.org/cfelton/fixed_point/raw/tip/examples/round/round_fix.png
.. _nearest round : https://bitbucket.org/cfelton/fixed_point/raw/tip/examples/round/round_nearest.png
.. _round : https://bitbucket.org/cfelton/fixed_point/raw/tip/examples/round/round_round.png
.. _convergent round : https://bitbucket.org/cfelton/fixed_point/raw/tip/examples/round/round_convergent.png


Example using the *fixbv* type.

    >>> x = fixbv(0, min=-1, max=1, res=2**-15) 
    >>> print(x, hex(x), repr(x))
    0.000000e+00 0x0 <0 (0.000000) W16.0> 

    >>> x = fixbv(2.5, min=-8, max=8, res=1/32.) 
    >>> print(x, hex(x), repr(x))
    2.500000e+00 0x50 <80 (2.500000) W13.9> 

    >>> x = fixbv(0.0333, min=-1, max=1, res=0.0001) 
    >>> print( x, hex(x), repr(x))
    3.332520e-02 0x222 <546 (0.033325) W15.0>


The /fixbv/ type does not automatically align or resize.  The 
*resize* funcition is used ot resize and align fixed-point
types.  The *resize* function has not been implemented in the
package yet (WIP).
