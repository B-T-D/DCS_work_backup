
def num_segments(petals):
    """Returns the number of segments to be used in drawing the flower."""
    return 8

def degrees(petals):
    """Returns the number of degrees to turn the turtle-pen at the start of
    each new segment."""
##    # Total interior angles of a regular polygon with n sides
##        # (Assuming that patterns holds that the 'flower' inscribes inside a
##        #   regular polygon of n sides where n = number of petals.)
##    interior_angles_sum = (petals - 2) * 180
##    print(interior_angles_sum)
##    # Individual interior angle:
##    interior_angle = interior_angles_sum / petals
##    print(f"each interior angle is {interior_angle} (from function)")
##    # Appears that the segment always hits the interior angle such that it needs
##    #   to come back "out" at a segment that would create a new angle of 1/3rd
##    # the size of the interior angle:
##    raw_turning_angle = interior_angle / 3
##    # For a left turn, the actual number of degrees to turn is the 'raw' minus
##    #   180:
##    degrees = 180 - raw_turning_angle
##    print(f"degrees from function is {degrees}")
##    return degrees
    return 1080/petals
