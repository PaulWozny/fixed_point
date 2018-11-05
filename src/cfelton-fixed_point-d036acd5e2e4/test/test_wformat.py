
from fixed_point._wformat import WFormat

def test_inst():
    e_wl,e_iwl,e_fwl = (8,4,3)
    W1 = WFormat(8,4,3)
    W2 = WFormat(8,4)

    W3 = WFormat(wl=8,iwl=4,fwl=3)

    for ww in (W1,W2,W3):
        wl,iwl,fwl = ww.fmt
        assert wl == e_wl
        assert iwl == e_iwl
        assert fwl == e_fwl
    
def test_add():
    # some basic adds
    W1 = WFormat(8,4)  # W8.4.3
    W2 = WFormat(8,4)  # W8.4.3
    Wa = W1+W2
    wl,iwl,fwl = Wa.fmt
    assert iwl == 5, '%s+%s==%s'  % (W1,W2,Wa)
    assert fwl == 3, '%s+%s==%s'  % (W1,W2,Wa)
    assert wl == 9, '%s+%s==%s'  % (W1,W2,Wa)

    W1 = WFormat(8,4)  # W8.4.3
    W2 = WFormat(8,3)  # W8.3.4
    Wa = W1+W2
    wl,iwl,fwl = Wa.fmt
    assert iwl == 5, '%s+%s==%s'  % (W1,W2,Wa)
    assert fwl == 4, '%s+%s==%s'  % (W1,W2,Wa)
    assert wl == 10, '%s+%s==%s'  % (W1,W2,Wa)

    W1 = WFormat(16,0)  # W16.0.15
    W2 = WFormat(16,0)  # W16.0.15
    Wa = W1+W2
    wl,iwl,fwl = Wa.fmt
    assert iwl == 1, '%s+%s==%s'  % (W1,W2,Wa)
    assert fwl == 15, '%s+%s==%s'  % (W1,W2,Wa)
    assert wl == 17, '%s+%s==%s'  % (W1,W2,Wa)

    W1 = WFormat(16,1)  # W16.1.14
    W2 = WFormat(16,3)  # W16.3.12
    Wa = W1+W2
    wl,iwl,fwl = Wa.fmt
    assert iwl == 4, '%s+%s==%s'  % (W1,W2,Wa)
    assert fwl == 14, '%s+%s==%s'  % (W1,W2,Wa)
    assert wl == 19, '%s+%s==%s'  % (W1,W2,Wa)

    # negative integer widths, fwl larger than the iwl
    W1 = WFormat(4,-4)
    W2 = WFormat(4,-4)
    Wa = W1+W2
    wl,iwl,fwl = Wa.fmt
    assert iwl == -3, '%s+%s==%s'  % (W1,W2,afmt)
    assert fwl == 7, '%s+%s==%s'  % (W1,W2,Wa)
    assert wl == 5, '%s+%s==%s'  % (W1,W2,Wa)

    # @todo: cross-over points when negative iwl becomes
    #        positive and vise-versa

    # negative fraction widths

    # @todo: cross-over points when negative fwl becomes
    #        positive and vise-versa

def test_sub():
    # some basic adds
    W1 = WFormat(8,4)  # W8.4.3
    W2 = WFormat(8,4)  # W8.4.3
    Wa = W1-W2
    wl,iwl,fwl = Wa.fmt
    assert iwl == 5, '%s+%s==%s'  % (W1,W2,Wa)
    assert fwl == 3, '%s+%s==%s'  % (W1,W2,Wa)
    assert wl == 9, '%s+%s==%s'  % (W1,W2,Wa)

    W1 = WFormat(8,4)  # W8.4.3
    W2 = WFormat(8,3)  # W8.3.4
    Wa = W1-W2
    wl,iwl,fwl = Wa.fmt
    assert iwl == 5, '%s+%s==%s'  % (W1,W2,Wa)
    assert fwl == 4, '%s+%s==%s'  % (W1,W2,Wa)
    assert wl == 10, '%s+%s==%s'  % (W1,W2,Wa)

    W1 = WFormat(16,0)  # W16.0.15
    W2 = WFormat(16,0)  # W16.0.15
    Wa = W1-W2
    wl,iwl,fwl = Wa.fmt
    assert iwl == 1, '%s+%s==%s'  % (W1,W2,Wa)
    assert fwl == 15, '%s+%s==%s'  % (W1,W2,Wa)
    assert wl == 17, '%s+%s==%s'  % (W1,W2,Wa)    

def test_mul():
    W1 = WFormat(8,4)  # W8.4.3
    W2 = WFormat(8,4)  # W8.4.3
    Wa = W1*W2
    wl,iwl,fwl = Wa.fmt
    assert iwl == 9, '%s+%s==%s'  % (W1,W2,Wa)
    assert fwl == 6, '%s+%s==%s'  % (W1,W2,Wa)
    assert wl == 16, '%s+%s==%s'  % (W1,W2,Wa)
    

if __name__ == '__main__':
    test_inst()
    test_add()
    test_sub()
    test_mul()
