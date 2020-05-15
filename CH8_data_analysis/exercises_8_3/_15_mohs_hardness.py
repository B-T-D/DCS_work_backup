def hardness(rocks):
    """
    Args:
        rocks (list): List of two-element tuples. Where first element of each
            tuple is name of a rock or mineral, and second is its hardness on
            mohs hardness scale. 

    Returns:
        (dict): Dictionary organizing the rocks and minerals in such a list
            into four categories: soft 1-3, medium 3.1-5, hard 5.1-8, very
            hard 8.1-10.
    """
    dict = {'soft': [], 'medium': [], 'hard': [], 'very hard': []}
    for rock in rocks:
        name = rock[0]
        hardness = rock[1]
        if hardness <= 3:
            dict['soft'].append(name)
        elif hardness <=5:
            dict['medium'].append(name)
        elif hardness <=8:
            dict['hard'].append(name)
        elif hardness > 8:
            dict['very hard'].append(name)
    return dict

rocks = [('talc', 1), ('lead', 1.5), ('copper', 3), ('nickel', 4),
         ('silicon', 6.5), ('emerald', 7.5), ('boron', 9.5), ('diamond', 10)]

dict = hardness(rocks)
print(dict)
        
