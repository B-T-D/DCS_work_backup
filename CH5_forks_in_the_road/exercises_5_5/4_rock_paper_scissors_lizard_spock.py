
def game(player_1, player_2):
    """Decides who wins in a game of rock, paper, scissors, lizard, spock.
    Args:
        player_1 (str): String with value of one of 'rock', 'paper', 'scissors',
            'lizard', or 'spock'.
        player_2 (str): String with value of one of the same options.

    Returns:
        (int): 1 if player 1 wins, -1 if player 2 wins, or 0 if they tie.
    """
    # Confirm valid inputs and return error rather than zero:
####    options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
####    player_1_error = True
####    player_2_error = True
####    for option in options:
####        print(f"option is {option}. Player 1 is {player_1}. Player 2 is {player_2}.")
####        if player_1 == option:
####            player_1_error = False
####            print(f"no player 1 error. player_1_error = {player_1_error}")
####        if player_2 == option:
####            player_1_error = False
####    if (player_1_error == True) or (player_2_error == True):
####        message = "Bad input(s)"
####        print(message)
####        return message
    
    
    outcome = None 
    if player_1 == player_2:
        outcome = 0
    elif player_1 == 'scissors':
        if player_2 == 'paper' or player_2 == 'lizard': # Scissors bets lizard and paper
            outcome = 1
        elif player_2 == 'rock' or player_2 == 'spock': # Scissors loses to rock and spock
            outcome = -1    
    elif player_1 == 'paper':
        if player_2 == 'rock' or player_2 == 'spock':
            outcome = 1
        elif player_2 == 'scissors' or player_2 == 'lizard':
            outcome = -1
    elif player_1 == 'rock':
        if player_2 == 'scissors' or player_2 == 'lizard':
            outcome = 1
        elif player_2 == 'paper' or player_2 == 'spock':
            outcome = -1
    elif player_1 == 'lizard':
        if player_2 == 'spock' or player_2 == 'paper':
            outcome = 1
        elif player_2 == 'rock' or player_2 == 'scissors':
            outcome = -1
    elif player_1 == 'spock':
        if player_2 == 'scissors' or player_2 == 'rock':
            outcome = 1
        elif player_2 == 'lizard' or player_2 == 'paper':
            outcome = -1
    return outcome

def sol_man():
    """Books way is better. Test for tie. Then test every possible way there
    could be a player 1 win. If none found, return a player 2 win."""

    if player_1 == player_2:
        result = 0
    if player_1 == 'scissors' and (player_2 == 'paper' or player_2 == 'lizard'):
        result = 1
    elif player_1 == 'paper' and (player_2 == 'rock' or player_2 == 'spock'):
        result = 1
    elif player_1 == 'rock' and (player_2 == 'lizard' or player_2 == 'scissors'):
        result = 1
    elif player_1 == 'lizard' and (player_2 == 'spock' or player_2 == 'paper'):
        result = 1
    elif player_1 == 'spock' and (player_2 == 'scissors' or player_2 == 'rock'):
        result = 1
    else:
        result - -1
    return result

def main():
    valid_inputs = {'r': 'rock',
                    'p': 'paper',
                    's': 'scissors',
                    'z': 'lizard',
                    'v': 'spock'}
    print(f"Valid inputs are {valid_inputs}")
    player_1 = input('Player1: ')
    player_2 = input('Player2: ')

    for key in valid_inputs.keys():
        if key == player_1:
            player_1 = valid_inputs[key]
        if key == player_2:
            player_2 = valid_inputs[key]

    outcome = game(player_1, player_2)

    if outcome == 1:
        print('Player 1 wins!')
    elif outcome == -1:
        print('Player 2 wins!')
    else:
        print('Tie or invalid input(s).')

def test_all():
    options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    pairs = [
        ('rock', 'rock'),
        ('rock', 'paper'),
        ('rock', 'scissors'),
        ('rock', 'lizard'),
        ('rock', 'spock'),
        ('paper', 'paper'),
        ('paper', 'scissors'),
        ('paper', 'lizard'),
        ('paper', 'spock'),
        ('scissors', 'scissors'),
        ('scissors', 'lizard'),
        ('scissors', 'spock'),
        ('lizard', 'lizard'),
        ('lizard', 'spock'),
        ('spock', 'spock')
        ]

    print(f"player_1| player_2|outcome")
    for pair in pairs:
        outcome = game(pair[0], pair[1])
        print(f"{pair[0]} | {pair[1]}| {outcome}  ")

def test_against_sol_man():
    pairs = [
        ('rock', 'rock'),
        ('rock', 'paper'),
        ('rock', 'scissors'),
        ('rock', 'lizard'),
        ('rock', 'spock'),
        ('paper', 'paper'),
        ('paper', 'scissors'),
        ('paper', 'lizard'),
        ('paper', 'spock'),
        ('scissors', 'scissors'),
        ('scissors', 'lizard'),
        ('scissors', 'spock'),
        ('lizard', 'lizard'),
        ('lizard', 'spock'),
        ('spock', 'spock')
        ]
    my_outcomes = {}
    for pair in pairs:
        my_outcomes[pair] = game(pair[0], pair[1])

    book_outcomes = {}
    for pair in pairs:
        book_outcomes[pair] = game(pair[0], pair[1])

    print(my_outcomes == book_outcomes)

##main()
##test_all()

test_against_sol_man()
    
