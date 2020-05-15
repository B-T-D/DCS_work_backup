def winner(votes):
    """Returns the majority vote between yea and nay in a list of strings
    all of which have one of those two values. Returne 'tie' if tie.
    """
    yeas = 0
    nays = 0
    for v in votes:
        if v == 'yea':
            yeas += 1
        elif v == 'nay':
            nays += 1
        else:
            return None # the inputs were bad if this is reached
    winner = ''
    if yeas > nays:
        winner = 'yea'
    elif nays > yeas:
        winner = 'nay'
    else:
        winner = 'tie'
    return winner

votes  = ['yea', 'nay', 'yea']
print(winner(votes))

votes.append('nay') # to create a tie
print(winner(votes))
