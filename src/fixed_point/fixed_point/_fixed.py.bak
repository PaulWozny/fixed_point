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
Fixed point model
"""

import pdb
import math
import copy

import myhdl

from _fixbv import fixbv
from _wformat import WFormat as W
from _modes import ROUND_MODES
#from _misc import convert_format

class fixed(fixbv):
    """
    This is a fixed-point integer model.  This is a subclass of
    the fixbv.  The main difference for this fixed point object
    is that it does autopromotion.  The class will only override
    the mathmatical operators.

    Some short-hand notation used
      wl   -- Word Length
      iwl  -- Integer Word Length
      fwl  -- Fractional Word Length
      fmt  -- Format (W-format)

      @todo: remove the following, use full name
      rm   -- Round Mode
      om   -- Overflow Mode


    """

    def __init__(self,
                 value, min=None, max=None, res=None,
                 format=(None,None),         # W format (wl,iwl,fwl)
                 round_mode='convergent',    # Type of rounding to perform
                 overflow_mode='saturate'):  # Type of overflow to perform
        
        # Use the fixbv constructor
        super(fixed, self).__init__(value, min, max,
                                    res, format,
                                    round_mode, overflow_mode)

    def __repr__(self):
        rs = "fixed(%f, "%(self._fval)
        wl,iwl,fwl = self._W.fmt
        fwl = wl-iwl-1
        rs += " format=W(%d,%d,%d), " % (wl,iwl,fwl)
        rs += ")"
        return rs
    
    def __str__(self):
        fstr = "%f" % (self._fval)
        return fstr
    
    # ~~~[setters and getters]~~~

    # ~~~[Overloaded Operators]~~~
    def __copy__(self):
        retval = fixed(self._fval,
                       min=self.min, max=self.max, res=self.res,
                       round_mode=self.round_mode,
                       overflow_mode=self.overflow_mode)
        return retval
    
    def __deepcopy__(self, visit):
        retval = fixed(self._fval,
                       min=self.min, max=self.max, res=self.res,
                       round_mode=self.round_mode,
                       overflow_mode=self.overflow_mode)
        return retval
    
    # Mathimatical operators
    def __mul__(self, other):

        # if the other is a float force it to the same size
        if isinstance(other,float):
            other = fixed(other, format=self.W,
                          round_mode=self.round_mode,
                          overflow_mode=self.overflow_mode)
            
        elif isinstance(other, (int,long,intbv)):
            fmax = other if other > 0 else 0
            fmin = other if other < 0 else 0
            other = fixed(other,min=fmin,max=fmax+1,res=0)
            
        assert isinstance(other, (fixed,fixbv)), "invalid multiplier"
        W = self.W*other.W

        retval = fixed(0,W=W,round_mode=self.round_mode,
                       overflow_mode=self.overflow_mode)

        # do the normal integer multiply
        retval._val = int(self)*int(other)
                
        return retval


    def __div__(self, other):
        # if the other is a float force it to the same size
        if isinstance(other,float):
            other = fixed(other, format=self.W,
                          round_mode=self.rm, overflow_mode=self.om)
            
        elif isinstance(other, (int,long,intbv)):
            fmax = other if other > 0 else 0
            fmin = other if other < 0 else 0
            other = fixed(other,min=fmin,max=fmax+1,res=0)
            
        assert isinstance(other, (fixed,fixbv)), "invalid divide"
        W = self.W*other.W

        retval = fixed(0,W=W,round_mode=self.round_mode,
                       overflow_mode=self.overflow_mode)

        # do the normal integer multiply
        retval._val = int(self)/int(other)

        return retval
        
    def __add__(self, other):
        """
        Fixed point addition c = a + b
        First promote a and b so that the a and b integer widths and
        fractional widths match.
        """
        a = fixed(float(self),format=self)
        if isinstance(other, float):
            b = fixed(other)
        elif isinstance(other,(int,long)):
            bmin = 0 if other > 0 else other
            bmax = other+1 if other > 0 else 0
            b = fixed(other,min=bmin,max=bmax,res=0)
        else:
            b = fixed(float(other),format=other)

        # get the maximum widths
        iwl = max(a._iwl, b._iwl)
        fwl = max(a._fwl, b._fwl)
        wl = iwl+fwl+1

        a._grow(W(wl,iwl,fwl))
        b._grow(W(wl,iwl,fwl))
        c = fixed(0,format=W(wl+1,iwl+1,fwl))
        c._val = a._val + b._val
        
        return c


    def __sub__(self, other):
        """
        Fixed point addition c = a + b
        First promote a and b so that the a and b integer widths and
        fractional widths match.
        """
        a = fixed(float(self),format=self)
        if isinstance(other, float):
            b = fixed(other)
        elif isinstance(other,(int,long)):
            bmin = 0 if other > 0 else other
            bmax = other+1 if other > 0 else 0
            b = fixed(other,min=bmin,max=bmax,res=0)
        else:
            b = fixed(float(other),format=other)

        # get the maximum widths
        iwl = max(a._iwl, b._iwl)
        fwl = max(a._fwl, b._fwl)
        wl = iwl+fwl+1

        a._grow(W(wl,iwl,fwl))
        b._grow(W(wl,iwl,fwl))
        c = fixed(0,format=W(wl+1,iwl+1,fwl))
        c._val = a._val - b._val
        
        return c

    # @todo
    #def __pow__(self, other):        

    # The shift operators are not implemented for the
    # /fixed/ type.  The handling of the shifts will be
    # passed to the base classes and will return an int
    # and not a new /fixed/

    # ~~~[local functions]~~~
    def _grow(self,format):
        """ Helper function 
        """
        wl,iwl,fwl = convert_format(format)
        assert wl >= self._wl
        assert iwl >= self._iwl
        assert fwl >= self._fwl

        val = self._val
        val = val << (fwl-self._fwl)
        self.W.fmt = (wl,iwl,fwl)
        self._val = val            

def convert_format(fmt):
    if isinstance(fmt,(fixed,fixbv)):
        wl,iwl,fwl = fmt.W.fmt
    elif isinstance(fmt,W):
        wl,iwl,fwl = fmt.fmt
    elif isinstance(fmt,(list,tuple)):
        if len(fmt) == 2:
            wl,iwl = fmt
            fwl = wl-iwl-1
        elif len(fmt) == 3:
            wl,iwl,fwl = fmt
        else:
            raise TypeError("Incorrect format")
    else:
        raise TypeError("Expected type fixed, fixbv, or WFormat not %s"%(type(fmt)))

    return wl,iwl,fwl
