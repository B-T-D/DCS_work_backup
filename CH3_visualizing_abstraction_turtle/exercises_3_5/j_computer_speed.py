"""
Ex 3.5.10
2020-03-28 20:43
"""

def time(instructions, gigahertz):
    """
    Computes the number of seconds needed to execute a given number of
    instructions on a computer with clock speed of given number of GHz,
    assuming each instruction takes 3 clock ticks to execute.
    
    Args:
        instructions (float): Number of instructions to be executed.
        gigahertz (float): Number of billions of times per second the clock
            ticks.
    Returns:
        (float) : Number of seconds needed to execute n instructions at a rate
            of g GHz.
    """
    
    ticks_per_inst = 3 # Prompt says assume a single instruction requires 3
        #   ticks to execute.
        # AK: Could've just done instructions * 3 / (gigahertz * 1e9)
    return instructions / inst_per_sec(gigahertz, ticks_per_inst)

def inst_per_sec(gigahertz, ticks_per_inst):
    ticks_per_second = gigahertz * 1e9
    return ticks_per_second / ticks_per_inst

print(time(1e9, 3))
