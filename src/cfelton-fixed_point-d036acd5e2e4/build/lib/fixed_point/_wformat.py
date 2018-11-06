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
"""

class WFormat(object):
    """
    Object to handle the W-format for fixed-point objects.
    By creating a class math can be performed on the \"W\".
    This can be useful when working with the fixbv and
    performning fixed-point alignment and auto-promotion in
    the elaboration phase.
    """

    def __init__(self,*fmt,**kwfmt):#,wl=None,iwl=None,fwl=None):
        assert len(fmt) <= 3
        for lk,lv in kwfmt.items():
            assert lk in ('wl','iwl','fwl'), "Invalid keyword argument %s"%(lk)
        if len(fmt) == 0:
            wl,iwl,fwl = (kwfmt['wl'],kwfmt['iwl'],kwfmt['fwl'],)
            fmt = (wl,iwl,fwl) if fwl is not None else (wl,iwl)
        #print(fmt)
        #print('WF: %s'%(str(fmt)))
        self.fmt = fmt

    #def __call__(self):
    #    return self._wl,self._iwl,self._fwl

    # @todo: use 'format', explicit, name and not fmt it is
    #        more consistent with the fixbv implementation
    @property
    def fmt(self):
        return self._wl,self._iwl,self._fwl
    @fmt.setter
    def fmt(self,format):
        if isinstance(format,tuple):
            if len(format) == 2:
                wl,iwl = format
                fwl = wl-iwl-1
            elif len(format) == 3:
                wl,iwl,fwl = format
            else:
                raise TypeError, "Invalid W format"
        elif isinstance(format, Wformat):
            wl = val._wl
            iwl = val._iwl
            fwl = val._fwl
        else:
            raise TypeError, "Invalid type %s"%(type(format))
        #print('setter %d,%d,%d'%(wl,iwl,fwl))
        assert wl == iwl+fwl+1, 'Invalid %d,%d,%d'  % (wl,iwl,fwl)
        self._wl = wl
        self._iwl = iwl
        self._fwl = fwl

    @property
    def format(self):
        return self.fmt
    @format.setter
    def format(self,val):
        self.fmt = val

    def align(self, other):
        """ """
        wl = self._wl
        iwl = self._iwl
        fwl = self._fwl
        
        if isinstance(other, Wformat):
            iwl = max(iwl, other._iwl)
            fwl = max(fwl, other._fwl)

            self.fmt  = (wl, iwl)
            other.fmt = (wl, iwl)
            
        elif isinstance(other, (list, tuple)):
            assert isinstance(ii,Wformat)
            for ii in other:
                iwl = max(iwl, ii._iwl)
                fwl = max(fwl, ii._fwl)
            wl = iwl+fwl+1
            for ii in other:
                ii.fmt = (wl,iwl)
                
        else:
            raise TypeError, "Align requires  WFormat, list or tuple type"

    def __str__(self):
        s = "WFormat(%d,%d,[%d])" % (self._wl, self._iwl, self._fwl)
        return s
    
    def __repr__(self):
        s = "WFormat(%d,%d,[%d])" % (self._wl, self._iwl, self._fwl)
        return s

    def __getitem__(self, key):
        if key == 0:
            val = self._wl
        elif key == 1:
            val = self._iwl
        elif key == 2:
            val = self._fwl
        else:
            raise AssertionError, "Invalid index %d %s" % (key, type(key))

        return val
    # @todo getitem setitme wl, iwl, fwl
    # @todo getitem setitem Wformat[0] = iwl
    #                       Wformat[1] = fwl
    
    def __add__(self, other):
        assert isinstance(other,WFormat), \
               "Invalid type for other %s" %  (type(other))
        # @todo: negative values of iwl and fwl need to be
        #        handled, if iwl is negative fwl will be
        #        incremented.  If fwl-wl-1 == 0 then increment
        #        the iwl

        # get the current largest
        iwl = max(self._iwl, other._iwl)+1
        fwl = max(self._fwl, other._fwl)
        wl = iwl+fwl+1
        #print('A: ',wl,iwl,fwl)
        return WFormat(wl,iwl,fwl)

    def __sub__(self, other):
        assert isinstance(other,WFormat), \
               "Invalid type for other %s" %  (type(other))
        #  @todo: negative values of iwl and fwl
        iwl = max(self._iwl,other._iwl)+1
        fwl = max(self._fwl,other._fwl)
        wl = iwl+fwl+1
        #print('S: ',wl,iwl,fwl)
        return WFormat(wl,iwl,fwl)

    def __mul__(self, other):
        assert isinstance(other,WFormat), \
               "Invalid type for other %s" %  (type(other))
        #  @todo: negative values of iwl and fwl
        wl = self._wl+other._wl
        fwl = self._fwl+other._fwl
        iwl = wl-fwl-1
        #print('M: ',wl,iwl,fwl)
        return WFormat(wl,iwl,fwl)

