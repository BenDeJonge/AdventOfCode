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
  Created on Mon Dec 12 22:15:07 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Rock-Paper-Scissors result calculator given known moves for both players.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from enum import IntEnum
from utils import read_data_generator, get_basename

#-- L O G I C -----------------------------------------------------------------

class Result(IntEnum):
    """Container for scores associated with each result."""
    
    Win  = 6
    Draw = 3
    Loss = 0

class Play(IntEnum):
    """Container for scores associated with each play."""
    
    Rock     = 1
    Paper    = 2
    Scissors = 3

def translate_to_rps(names : str) -> dict[Play, ...]:
    """Translate input codes to rock-paper-scissors moves."""
    return dict(zip(names, (Play.Rock, Play.Paper, Play.Scissors)))

def win_loss_draw(opponent : Play, player : Play, 
                  wins_against : dict[Play, ...]) -> Result:
    """Find the result given two moves and a results table."""
    if player == wins_against[opponent]:
        return Result.Win
    elif opponent == wins_against[player]:
        return Result.Loss
    else:
        return Result.Draw

#-- C O N S T A N T S ---------------------------------------------------------

# Score table for winning play against each play.
wins_against = {
    Play.Rock     : Play.Paper,
    Play.Paper    : Play.Scissors,
    Play.Scissors : Play.Rock} 

# Translate codes to rock-paper-scissors moves for player and opponent.
opponent_to_rps, player_to_rps = (translate_to_rps(names) for names in ('ABC', 'XYZ'))

#-- M A I N   L O O P ---------------------------------------------------------

# Get codes for each round. Get moves for played codes. Sum up scores.
current_score = 0
for line in read_data_generator(get_basename(__file__)):
    opponent, player = line.strip().split(' ')
    opponent = opponent_to_rps[opponent]
    player = player_to_rps[player]
    current_score += (win_loss_draw(opponent, player, wins_against) + player)
    
print(current_score)