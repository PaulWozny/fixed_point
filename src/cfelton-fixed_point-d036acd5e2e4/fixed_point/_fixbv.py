#
# Copyright (c) 2009-2013 Christopher L. Felton
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Fixed-point object for MyHDL.
"""

import sys
import math
import copy

import myhdl
from _wformat import WFormat
from _modes import ROUND_MODES,OVERFLOW_MODES
from _misc import check_myhdl_version

SignalType = check_myhdl_version()


class fixbv(myhdl.intbv):
    """
    Some short-hand notation used
      wl   -- Word Length
      iwl  -- Integer Word Length
      fwl  -- Fractional Word Length
      W    -- Format (W-format)

      @todo change to the long names
      rm   -- Round Mode
      om   -- Overflow Mode


    """
    
    def __init__(self,
                 value,                     # initial default value
                 min = None,                # Min value required
                 max = None,                # Max value required
                 res = None,                # Resolution required
                 format = None,             # If preferred W notation W(wl,iwl)
                 
                 # these parameters only apply to the initial value rounding
                 # and overflow for the fixbv object
                 round_mode = 'floor',      # Type of rounding to perform
                 overflow_mode = 'saturate' # Type of overflow to perform
                 ):
        """
        @todo comments
        Overall bit with is iwl + fwl + 1

         Parameters
         ----------
           value : initial value
           min : Minumum value 
           max : Maximum value
           res : Resolution of the fixed-point type
           format : Explicit (wl,iwl) setting, WFormat
           round_mode : Initial value rounding method
                       rounding types
                         ceil,floor,fix,nearest,round,convergent
    
        """

        value = float(value)
        
        # If the user does not specifiy ranges, determine the required
        # range.  Convert the bit lengths to the proper specification
        # for checking and extracting.  The bit lengths will be
        # recalculated based on the property specs and checked against
        # those supplied.
        incomplete_spec = [kw is None for kw in (min,max,res)]
        if True in incomplete_spec:
            try:
                if isinstance(format,WFormat):
                    self._W = copy.copy(format)
                elif isinstance(format,fixbv):
                    self._W = copy.copy(format._W)
                elif isinstance(format, (tuple,list)):
                    self._W = WFormat(*format)
                else:
                    raise ValueError("Invalid format type %s"%(type(format)))
                wl,iwl,fwl = self._W.fmt
                min=-2**iwl; max=2**iwl; res=2.0**-fwl 
            except TypeError:
                self._W = None
                min,max,res = self._calc_min_max_res(value)
        else:
            self._W = None
                
        # validate the range and resolution
        if max < 1 or abs(min) < 1:
            raise ValueError, "Maximum and Minimum  has to be 1 or greater"
        if max == None or not isinstance(max, (int, long, float)):
            raise ValueError, "Maximum has to be provided, max=%s" % (str(max))
        if min == None or not isinstance(min, (int, long, float)):
            raise ValueError, "Minimum has to be provided, min=%s" % (str(min))
        if res == None or not isinstance(res, float):
            raise ValueError, "Resolution has to be provided, res=%s" % (str(res))

        if not round_mode in ROUND_MODES:
            raise ValueError, "Round mode %s not supported!" % round_mode
        if not overflow_mode in OVERFLOW_MODES:
            raise ValueError, "Overflow mode %s not supported!" % overflow_mode

        # save the round and overflow modes
        self._rm = round_mode
        self._om = overflow_mode

        # Calculate the integer and fractional widths
        ival = abs(min) if abs(min) > max else max
        
        (niwl, nfwl) = self._calc_width(ival, res)
        nwl = niwl+nfwl+1
        
        if self._W is None:
            self._W = WFormat(nwl,niwl)
        else:
            wl,iwl,fwl = self._W.fmt
            assert wl == nwl, "calculation error, word length"
            assert iwl == niwl, "calculation error, integer word length"
            assert fwl == nfwl, "calculation error, fractional word length"

                        
        # We want a signed number but we don't want to force any
        # notion of a fixed point value to the lower levels.  From
        # the intbv point of view it only knows that it is a signed
        # integer, this is enough information to enforce the rules.
        # But what should the min and max values be?  Well it should
        # what ever the min/max for the number of bits we are creating.        
        nrbits = self._iwl + self._fwl + 1
        min    = -1 * 2**(nrbits-1)
        max    = 2**(nrbits-1) 
        myhdl.intbv.__init__(self, 0, min=min, max=max)
        self._fval = value

        if self._nrbits != nrbits:
            raise "ERROR: intbv number of bits != fixbv number of bits %d,%d" \
                  % (self._nrbits, nrbits)

        # make sure things were setup ok
        self._handleBounds()
        
    ###################################################################### 
    # properties
    ######################################################################
    def _handleBounds(self):
        """ Check the bounds """
        myhdl.intbv._handleBounds(self)
        
    @property
    def _fval(self):
        return self._to_float()
    @_fval.setter
    def _fval(self,val):
        self._val = self._from_float(val)

    @property
    def _wl(self):
        wl,iwl,fwl = self._W.fmt
        return wl
    
    @property
    def _iwl(self):
        wl,iwl,fwl = self._W.fmt
        return iwl
    
    @property
    def _fwl(self):
        wl,iwl,fwl = self._W.fmt
        return fwl
    
    @property
    def round_mode(self):
        return self._rm

    @property
    def overflow_mode(self):
        return self._om

    @property
    def res(self):
        return 2**(-1*self._fwl)
    
    @property
    def min(self):
        return -2**(self._iwl)

    @property
    def max(self):
        return 2**(self._iwl)

    @property
    def W(self):
        return self._W
    @W.setter
    def W(self,val):
        self._W.fmt = val
        self._nrbits = self._wl
    
    ###################################################################### 
    # overloaded functions
    ######################################################################
    def __copy__(self):
        retval = fixbv(self._fval, self.min, self.max, self.res,
                       W=self.W,
                       round_mode=self._rm, overflow_mode=self._om)
        return retval
    
    def __deepcopy__(self, visit):
        retval = fixbv(self.fValue, self.min, self.max, self.res,
                       W=self.W,
                       round_mode=self._rm, overflow_mode=self._om)
        return retval

    # __getitem__ and __setitem (bit access) will be handled by
    # the inherited intbv.  The bit access will not change the
    # type (ie W16.0) or the structure (iwl and fwl) of the
    # fixed point number.
    #
    # NOTE #1:  The get item (e.g. x[2]) will return a intbv and
    #           not a fixbv.  This seems appropriate, if we are
    #           taking a slice out of our number we are breaking
    #           the representation, either need to start new or
    #           using the bits as something else.
    #
    # NOTE #2 : VHDL and Verilog use negative indexes for bits
    #           right of the "point" see if the same behavior can
    #           be implemented for this object.
    #
    # @todo: To allow bit indexing or not?  It really breaks the
    #        fixed point representation and handling, leaning towards
    #        not allowing bit indexing
    def __setitem__(self, key, val):
        if isinstance(val, fixbv):
            v = val._val
        else:
            v = val
        # @todo: convert negative keys to the correct bit index
        myhdl.intbv.__setitem__(self, key, v)

    def __getitem__(self, key):
        # when slicing into a fixbv not trying to maintain any notion
        # of integer fractional, simply returning the integer value for
        # those bits, unless it is the full-range.
        slc = myhdl.intbv(self._val, _nrbits=self._nrbits)
        # @todo: convert negative keys to the correct bit index
        return slc.__getitem__(key)
        
    def __repr__(self):
        # fixbv(_fval, W=(%d,%d,%d))
        rs = "fixbv(%f, "%(self._fval)
        wl,iwl,fwl = self._W.fmt
        fwl = wl-iwl-1
        rs += " format=W(%d,%d,%d), " % (wl,iwl,fwl)
        rs += ")"
        # @todo: ? add integer value somewhere?
        return rs
    
    def __str__(self):
        # For very large bit widths the resolution of the fixbv
        # will exceed those of a 64 bit value.  Need to use something
        # more power when "displaying" the values, use the Decimal
        # object to create a more accurate version of the underlying
        # value.
        # @todo: use *Decimal* and determine the number of of
        #        10s digits required.
        #         intp = Decimal(self._iival) + 2**Decimal(-self._ifval)
        fstr = "%f" % (self._fval)
        return fstr

    def __hex__(self):
        return hex(self._val)

    def __float__(self):
        return self._fval
    
    # The mathematical and bit operations will be handled by the underlying
    # intbv object.  This will be a different than the original implementation
    # which would adjust the bit widths of the output.  The intbv relies on
    # the designer to supply the correct bit-widths.  This is more appropriate
    # for conversion.  There are public functions provided instead that will
    # return fixbv with the correct sizes for the operation.
    def __mul__(self, other):
        """
        Utilize the underlying MyHDL intbv to handle the multiply.  The MyHDL
        mathimatical operations return a value and not a type so the assignements
        must be done such as:

        c[:] = a * b
        """
        if isinstance(other, fixbv):
            iW = self.W * other.W
        else:
            raise TypeError, "other must be fixbv: self*other"
            
        retval = fixbv(0, format=iW, round_mode=self.round_mode)
        mul = myhdl.intbv(self._val) * other
        retval.value = mul
        return mul #retval

    
    def __add__(self, other):
        """
        Fixed-point addition is no different than normal signed binary
        arithmetic.  Fixed-point mainly deals with the interpetation of the
        binary number.  But it does need the binary points to be aligned.  The
        burden of aligning the point is on the developer but this function will
        assert that the points are aligned.
        c[:] = a + b
        """
        if isinstance(other, fixbv):
            assert self._fwl == other._fwl, "Add: Points not aligned %s == %s" % (repr(self), repr(other))
            iW = self.W + other.W
        # @todo if other is not fixbv (int, long, intbv) convert to fixbv and
        # perform the addition
        else:
            raise TypeError, "other must be fixbv: self + other"

        retval = fixbv(0, format=iW, round_mode=self.round_mode)
        add = myhdl.intbv(self._val) + other
        retval.value = add
        return add #retval    

    
    def __sub__(self, other):
        """
        Same as addition just different
        c[:] = a - b
        """
        if isinstance(other, fixbv):
            assert self._fwl == other._fwl, "Sub: Points not aligned  %s == %s" % (repr(self), repr(other))
            iW = self.W + other.W
        # @todo if other is not fixbv (int, long, intbv) convert to fixbv and
        # perform the addition
        else:
            raise TypeError, "other must be fixbv: self*other"

        retval = fixbv(0, format=iW, round_mode=self.round_mode)
        sub = myhdl.intbv(self._val) - other
        retval.value = add
        return sub #retval

    def __div__(self, other):
        assert False, "TODO"

    # use the underlying myhdl shifts
    #def __lshift__(self, other):
    #    retval = fixbv(0, min=self.min, max=self.max, res=self.res,
    #                     round_mode=self.round_mode)
    #    new = myhdl.intbv.__lshift__(self, other)  # returns intbv
    #    retval.value = new._val
    #    return retval
    #
    #def __rlshift__(self, other):
    #    retval = fixbv(0, min=self.min, max=self.max, res=self.res,
    #                     round_mode=self.round_mode)
    #    new = myhdl.intbv.__rlshift__(self, other)  # returns intbv
    #    retval.value = new._val
    #    return retval
    #
    #def __rshift__(self, other):
    #    retval = fixbv(0, min=self.min, max=self.max, res=self.res,
    #                     round_mode=self.round_mode)
    #    new = myhdl.intbv.__rshift__(self, other)  # returns intbv
    #    retval.value = new._val
    #    return retval
    #
    #def __rrshift__(self, other):
    #    retval = fixbv(0, min=self.min, max=self.max, res=self.res,
    #                     round_mode=self.round_mode)
    #    new = myhdl.intbv.__rrshift__(self, other)  # returns intbv
    #    retval.value = new._val
    #    return retval

    
    ###################################################################### 
    # private methods
    ######################################################################
    def _calc_width(self, value, res=0):
        """Caclulate the iwl and fwl required for the value"""
        frac, integer = math.modf(value)

        if res < frac or frac == 0:
            frac = res
        
        if abs(integer) == 0:
            iw = 0
        else:
            iw = math.ceil(math.log(abs(integer), 2))

        if frac == 0:
            fw = 0
        else:
            fw = math.ceil(math.log(frac**-1, 2))

        return (int(iw), int(fw))


    def _calc_min_max_res(self, fval):
        """Given floating point number calculate min, max and resolution
        Given a floating point number calculate the resolution required to
        represent the floating-point in a fixed-point number.
        """
        if fval == 0:
            inbits = 1
            fnbits = 1
        else:
            frac, integer = math.modf(fval)
            frac = abs(frac)
            integer = abs(integer)
            try:
                # adds an extra bit
                if integer == 0:
                    inbits = 1
                else:
                    inbits = int(abs(math.floor(math.log(integer, 2)))) + 1

                # adds an extra bit
                if frac == 0:
                    fnbits = 1
                else:
                    fnbits = int(abs(math.floor(math.log(frac, 2)))) + 1
            except :
                print "Fractional %s Integer %s" % (frac, integer)
                print "Unexpected error:", sys.exc_info()[0]
                raise
            
        fnbits = 1 if fnbits == 0 else fnbits
        inbits = 1 if inbits == 0 else inbits
        max = 2**(inbits-1)
        min = -2**(inbits-1)
        res = 2**(-fnbits)
        #print "Calc limits %f --> fnbits %d inbits %d, max %f, min %f, res %f" % (fval, fnbits, inbits, max, min, res)

        # make sure limits are still applicable for the rounded version of fval
        # if the value doesn't fit need an extra integer bit.  This functions
        # is mainly used if bit constraints are not give (determine bit contraints
        # from value).  Adding extra bit (case of round_mode=truncate) is ok.
        if round(fval) >= max or round(fval) <= min:
            max = 2**(inbits+1)
            min = -2**(inbits+1)
        
        return min,max,res

    
    def _from_float(self, value):
        """Convert float value to fixed point"""
        retval = self._round(value) 
        retval = self._overflow(retval)
        return retval
        

    def _to_float(self):
        """Convert fixed point value to floating point number"""
        return float(self._val) / (2.0 ** self._fwl)


    def _overflow(self, value):
        """Handle overflow"""
        if self.overflow_mode == 'saturate':
            if value >= self._max:
                retval = self._max-1
            elif value <= self._min:
                retval = self._min
            else:
                retval = value
        elif self.overflow_mode == 'ring':
            raise NotImplementedError
        else:
            raise ValueError
        return retval
        
        
    def _round(self, value):
        """Round the initial value if needed"""
        # Scale the value to the integer range (the underlying representation)
        #print('   rnd[bs]: %f'%(value))
        value = value * 2.0**self._fwl
        #print('   rnd[as]: %f'%(value))
        
        if self.round_mode == 'ceil':
            retval = math.ceil(value)

        elif self.round_mode == 'fix':
            if value > 0:
                retval = math.floor(value)
            else:
                retval = math.ceil(value)
            #retval = int(value)

        elif self.round_mode == 'floor':
            retval = math.floor(value)

        elif self.round_mode == 'nearest':
            fval,ival = math.modf(value)
            if fval == .5:
                retval = int(value+1) if value > 0 else int(value-1)
            else:
                retval = round(value)

        elif self.round_mode == 'round':
            retval = round(value)
            
        elif self.round_mode == 'round_even' or self.round_mode == 'convergent':
            fval,ival = math.modf(value)
            abs_ival = int(abs(ival))
            
            if int(ival < 0):
                sign = -1
            else:
                sign = 1

            if (abs(fval) - 0.5) == 0.0:
                if abs_ival%2 == 0:
                    retval = abs_ival * sign
                else:
                    retval = (abs_ival + 1) * sign
            else:
                retval = round(value)

        else:
            raise TypeError, "ERROR: fixbv._round(): %s not supported round mode!" % self._rm

        return int(retval)


#-#    ###################################################################### 
#-#    # public methods
#-#    ###################################################################### 
#-#
#-#    def range(self):
#-#        """Print out the possbile value range of the number."""
#-#        min = -2**self._iwl
#-#        max = 2**self._iwl - 1.0 / 2.0**self._fwl
#-#        s = "W%01d.%d:" % (self._iwl, self._fwl)
#-#        s = s + " %f ... %f" % (min, max)
#-#        return s
#-#
#-#
#-#    def resolution(self):
#-#        """Return the resolution of the fixed-point number."""
#-#        res = 2**(-1.*self._fwl)
#-#        s = "%f" % (res)
#-#        return s
#-#
#-#        
#-#    def bit(self):
#-#        """Return number as a bit string."""
#-#        wl,iwl,fwl = self._W.fmt
#-#        return myhdl.bin(self, wl)
