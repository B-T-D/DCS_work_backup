from class_pair import Pair

def get_votes():
    """Get votes as input from user and return it as a pair object"""
    tally = Pair(0, 0)
    prompt = "Enter votes (q to quit):\n>>>"
    votes = input(prompt)
    while votes.lower() != 'q':
        votes = votes.split(',')
        votes = Pair(int(votes[0]), int(votes[1]))
        tally = tally.add(votes)
        votes = input(prompt)
    return tally

def main():
    tally = get_votes()
    print(f"Candidate 1: {tally.get_first()} votes") # tally object not subscriptable rn so must hard code
    print(f"Candidate 2: {tally.get_second()} votes")
   
main()
