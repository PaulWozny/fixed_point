
                  # round    :
ROUND_MODES = (   # towards  :
    'ceil',       # +infinity: always round up
    'fix',        # 0        : always down
    'floor',      # -infinity: truncate, always round down
    'nearest',    # nearest  : tie towards largest absolute value
    'round',      # nearest  : ties to +infinity
    'convergent', # nearest  : tie to closest even (round_even)
    'round_even', # nearest  : tie to closest even (convergent)
    )

def is_round_mode(mode):
    if mode.lower() in ROUND_MODES:
       found = True
    else:
        # @todo: does it match
        found = False        
    return found

OVERFLOW_MODES = (
    'saturate',
    'ring'
    )

def is_overflow_mode(mode):
    if mode.lower() in OVERFLOW_MODES:
        found = True
    else:
        # @todo: is there a close match?
        found = False
    return found

               
