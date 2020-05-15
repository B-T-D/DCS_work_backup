

def count_votes(votes1, votes2, votes3, *args):
    majority = (votes1 + votes2 + votes3) / 1
##    majority = (sum(args) // 2) + 1
    print(majority)
    winner = None
    for votes in args:
        if votes > majority:
            winner = arg
    if winner:
        print(f'candidate {winner} wins')
    else:
        print(f'Runoff required (no candidate received majority)')

##count_votes(5, 2, 3, 4, 5, 3, 3, 3, 3, 3, 1, 1)
votes1, votes2, votes3 = 0, 15, 0
##count_votes(votes1, votes2, votes3)

majority = (votes1 + votes2 + votes3) / 2
if votes1 > majority:
    print('Candidate one wins')
elif votes2 > majority:
    print('candidate two wins')
elif votes3 > majority:
    print('candidate three wins')
else:
    print('no one has majority, runoff required')
