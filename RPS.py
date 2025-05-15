# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random


def player(prev_play, opponent_history=[], bot=[0]):
    opponent_history.append(prev_play)

    guess = {'P': 'S', 'R': 'P', 'S': 'R'} 
    counter_response = {'R':'S','P':'R','S':'P'}


    if prev_play == '':
        #randomly choose a play
        prev_play = random.choice(list(guess.keys()))
        return guess[prev_play]
    elif len(opponent_history) >= 5:
        # Checking for Quincy's Sequence (R R P P S)
        if find_pattern(opponent_history, ['R', 'R', 'P', 'P', 'S']) != -1:
            bot[0] = 'quincy'

        print("Bot:", bot[0])

            
        
            
            
            
        
            
        
            

        guess = opponent_history[-2]
        return guess
    else:
        return guess[prev_play]


def default_player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess


def find_pattern(data, pattern):
    pattern_len = len(pattern)
    for i in range(len(data) - pattern_len + 1):
        if data[i:i+pattern_len] == pattern:
            return i  # Found at index i
    return -1  # Not found