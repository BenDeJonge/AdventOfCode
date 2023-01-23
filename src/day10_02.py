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
  Created on Wed Dec 21 00:01:59 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename
from day10_01 import Event

#-- C O N S T A N T S ---------------------------------------------------------

SCREEN_WIDTH = 40
sprite = 1
cycle = 0
signal_strength = 0
line = [' ',] * SCREEN_WIDTH

for instr in read_data_generator(get_basename(__file__), strip=True):
    e = Event(instr)
    while e.counter > 0:
        # Get the index of the pixel and see if it overlaps with the sprite.
        pixel = cycle % SCREEN_WIDTH
        if pixel in range(sprite-1, sprite+2):
            line[pixel] = '#'
        else:
            line[pixel] = '.'
        # Increment the cycle. Print the line if complete.
        cycle += 1
        if cycle % SCREEN_WIDTH == 0:
            print(''.join(line))
            line = ['.',] * SCREEN_WIDTH
        # Perform the events for the current cycle.
        e.count_down()
        sprite += e.get_effect()