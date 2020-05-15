
def fair(employee, ceo, ratio):
    """Decide whether the ration of CEO to employee pay is fair.
    Args:
        employee : Average employee pay
        ceo: CEO pay
        ratio: Ratio deemed fair

    Return:
        (bool): True if the ratio of CEO pay to employee pay is fair.
    """
    # Confirm that employee pay won't cause a division by zero error:
    if employee == 0:
        result = False
    else:
        result =(ceo / employee <= ratio)
    return result

def fair_shortcircuit(employee, ceo, ratio):
    """With short circuit evaluation, can simplify the whole function to..."""
    return (employee != 0) and (ceo / employee <= ratio)

def unfair(employee, ceo, ratio):
    """Decide whether the ratio of CEO to employee pay is unfair.

    Returns:
        (bool) : Boolean indicating whether ratio of CEO to employee pay is
        unfair.
    """
    if employee == 0:
        result = True
    else:
        result = (ceo / employee > ratio)
    return result

def unfair_shortcircuit(employee, ceo, ratio):
    return (employee == 0) or (ceo / employee > ratio)

print(fair(2, 6, 2))
print(unfair(2, 6, 2))
print(unfair_shortcircuit(2, 6, 2))


    
