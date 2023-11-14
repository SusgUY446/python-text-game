
import json

import time

def load_game():
    try:
        with open('game_state.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            'xp_level': 0,
            'game_level': 1,
            'inventory': {'item1': 10, 'item2': 5}
        }

saveState = load_game()

def save_game():
    while True:
        with open('save.json', 'w') as file:
            json.dump(saveState, file)
        time.sleep(300)  # saves every 5 minutes

