
import myhdl    

def check_myhdl_version():
    mver = myhdl.__version__
    if 'd' in mver:
        n,s = mver.split('d')
    else:    
        n = mver

    rev = float(n)
    if rev >= 0.7:
        SignalType = myhdl._Signal._Signal
    else:
        SignalType = myhdl.Signal

    return SignalType




