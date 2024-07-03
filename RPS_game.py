import random

def player(prev_play, opponent_history=[]):
    # Strategy 1: Random play on the first move
    if prev_play == "":
        return random.choice(['R', 'P', 'S'])
    
    # Strategy 2: Counter strategy based on opponent's last move
    if prev_play == 'R':
        return 'P'  # Paper beats Rock
    elif prev_play == 'P':
        return 'S'  # Scissors beats Paper
    elif prev_play == 'S':
        return 'R'  # Rock beats Scissors
    
    # Strategy 3: Pattern recognition and adaptation
    if len(opponent_history) >= 3:
        last_three_moves = opponent_history[-3:]
        if last_three_moves == ['R', 'P', 'S']:
            return 'R'  # Predict opponent will play 'R'
        elif last_three_moves == ['S', 'S', 'P']:
            return 'P'  # Predict opponent will play 'P'
        # Add more patterns as needed
    
    # Default: Random choice to add unpredictability
    return random.choice(['R', 'P', 'S'])

# Test against bots
from RPS_game import play, rock, paper, scissors, random_player

bots = [rock, paper, scissors, random_player]
num_games = 1000

for bot in bots:
    win_rate = play(player, bot, num_games)
    print(f"Win rate against {bot.__name__}: {win_rate}%")
    if win_rate >= 60:
        print("Passed the challenge against this bot!")
    else:
        print("Did not pass the challenge against this bot.")

# Ensure your player function performs well against all bots
