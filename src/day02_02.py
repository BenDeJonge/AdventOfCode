# -*- coding: utf-8 -*-
"""
...............................................................................

╔═════════════════════════════════════════════════════════════════════════════╗
║                             Copyright statement                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Confidential Information
  Copyright by imec
  imec vzw
  Kapeldreef 75
  3001 Leuven
  Belgium
  www.imec.be
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                  Creation                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Created on Mon Dec 12 23:16:29 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Rock-Paper-Scissors given the wanted result and the opponents move.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename
from day02_01 import Result, Play, translate_to_rps, wins_against

#-- C O N S T A N T S ---------------------------------------------------------

# Translate codes to moves for opponent.
opponent_to_rps = translate_to_rps('ABC')

# Translate codes to results for the player.
wanted_result = {
    'X' : Result.Loss,
    'Y' : Result.Draw,
    'Z' : Result.Win}

#-- L O G I C -----------------------------------------------------------------

def player_move_from_result(opponent : Play, result : Play,
                            wins_against : dict[Play, ...]) -> Play:
    """Get the players move given the opponent's and the wanted result."""
    # Reciprocal score table for each move.
    loses_to = {win : loss for loss, win in wins_against.items()}
    # Logic.
    if result == Result.Win:
        return wins_against[opponent]
    elif result == Result.Loss:
        return loses_to[opponent]
    else:
        return opponent

#-- M A I N   L O O P ---------------------------------------------------------

# Get codes for each round. Get move for opponent's code and result from player.
# Get player move from result. Sum up scores.
current_score = 0
for line in read_data_generator(get_basename(__file__)):
    opponent, player = line.strip().split(' ')
    opponent = opponent_to_rps[opponent]
    result = wanted_result[player]
    current_score += (result + player_move_from_result(opponent, result, wins_against))
    
print(current_score)