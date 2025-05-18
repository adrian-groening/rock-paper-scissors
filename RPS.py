
import random

def player(prev_play,
           opponent_history=[],
           bot=[0],
           history=[],
           my_opponent_history=[],
           count=[0],
           play_order=[{
               "RR": 0,
               "RP": 0,
               "RS": 0,
               "PR": 0,
               "PP": 0,
               "PS": 0,
               "SR": 0,
               "SP": 0,
               "SS": 0,
            }]):

    if count[0]==1000:
        opponent_history.clear()
        history.clear()
        count[0] = 0
        
    if prev_play != '':
        opponent_history.append(prev_play)
    
    guess = {'P': 'S', 'R': 'P', 'S': 'R'} 
    counter_response = {'R':'S','P':'R','S':'P'}
    inital_sequence = ['S', 'R', 'P', 'P', 'R', 'S', 'R', 'P', 'S', 'R']
    play = ''

    if len(opponent_history) == 0:
        play = inital_sequence[0]
        history.append(play)
        count[0] += 1
        return play
    if len(opponent_history) < 10:
        play = inital_sequence[len(opponent_history)-1]
        history.append(play)
        count[0] += 1
        return play

    if find_pattern(opponent_history, ['R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S']) != -1:
        bot[0] = 'quincy'
    if len(opponent_history) == 10:
        if most_frequent(opponent_history) == 'R':
            bot[0] = 'mrguesh'
    if opponent_history[1] == guess[history[0]] and opponent_history[2] == guess[history[1]] and opponent_history[3] == guess[history[2]] and opponent_history[4] == guess[history[3]] and opponent_history[5] == guess[history[4]] and opponent_history[6] == guess[history[5]] and opponent_history[7] == guess[history[6]] and opponent_history[8] == guess[history[7]] and opponent_history[9] == guess[history[8]]:
        bot[0] = 'kris'
    if bot[0] not in ['quincy', 'mrguesh', 'kris']:
        bot[0] = 'abbey'
    

    if bot [0] == 'quincy':
        if prev_play == 'S':
            history.append('P')
            count[0] += 1
            return 'P'
        elif prev_play == 'P' and opponent_history[-2] == 'P':
            history.append('R')
            count[0] += 1
            return 'R'
        elif prev_play == 'P' and opponent_history[-2] == 'R':
            history.append('S')
            count[0] += 1
            return 'S'
        elif prev_play == 'R' and opponent_history[-2] == 'R':
            history.append('S')
            count[0] += 1
            return 'S'
        elif prev_play == 'R' and opponent_history[-2] == 'S':
            history.append('P')
            count[0] += 1
            return 'P'
    if bot[0] == 'mrguesh':
        play = guess[most_frequent(history)]
        history.append(play)
        count[0] += 1
        return play
    if bot[0] == 'kris':
        play = guess[history[-1]]
        history.append(play)
        count[0] += 1
        return play
    if bot[0] == 'abbey':
        if not history[-1]:
            my_prev_play = 'R'
        else:
            my_prev_play = history[-1]
            
        my_opponent_history.append(my_prev_play)

        if len(my_opponent_history) >= 2:
            last_two = "".join(my_opponent_history[-2:])
            if last_two in play_order[0]:
                play_order[0][last_two] += 1
        else:
            last_two = ""

        potential_plays = [last_two[-1:] + move for move in ['R', 'P', 'S']] if last_two else []


        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }

        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1]
        else:
            prediction = random.choice(['R', 'P', 'S'])

        opponent_expected_play = {'P': 'S', 'R': 'P', 'S': 'R'}[prediction]


        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        final_play = ideal_response[opponent_expected_play]

        if count[0] < 300:
            play = random.choice(['R', 'P', 'S'])
        elif count[0] < 600:
            play = final_play
        elif count[0] < 900:
            play = random.choice(['R', 'P', 'S'])
        else:
            play = final_play

        history.append(play)
        count[0] += 1
        return play
        
        



    
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

def most_frequent(history):
    last_ten = history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)
    return most_frequent


    

