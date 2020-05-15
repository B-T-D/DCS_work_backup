

def assign_gp(score):
    """Returns the grade point equivalent of score.
    Args:
        score (int): A score between 0 and 100

    Returns:
        (int): The equivalent grade-point value.
    """

    if score >= 90:
        return 4
    if score >= 80:
        return 3
    if score >= 70:
        return 2
    if score >= 60:
        return 1
    return 0

print(assign_gp(78))
