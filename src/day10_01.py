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
  Created on Tue Dec 20 22:58:50 2022
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

#-- C O N S T A N T S ---------------------------------------------------------

MAX_SIZE = 2
sprite = 1
target_cycles = (20, 60, 100, 140, 180, 220)

#-- L O G I C -----------------------------------------------------------------

class Event:
    """An Event with an effect and a counter."""
    
    def __init__(self, line):
        self.line = line
        self.effect, self.counter = self.parse_instruction(self.line)
    
    def __repr__(self) -> str:
        """Get a string represenation of the Event."""
        return f'Event({self.effect}) in {self.counter}'
    
    def parse_instruction(self, line) -> (int, int):
        """Get the required action and counter from the instruction."""
        parts = line.split()
        if parts[0] == 'noop':
            return 0, 1
        elif parts[0] == 'addx':
            return eval(parts[1]), 2

    def count_down(self):
        """Reduce the counter."""
        self.counter -= 1
    
    def get_effect(self):
        """Get the Event effect if the counter is 0."""
        if self.counter == 0:
            return self.effect
        return 0

#-- M A I N   L O O P ---------------------------------------------------------

if __name__ == '__main__':

    cycle = 0
    signal_strength = 0
    
    for line in read_data_generator(get_basename(__file__), strip=True):
        e = Event(line)
        while e.counter > 0:
            cycle += 1
            if cycle in target_cycles:
                signal_strength += (cycle * sprite)
            e.count_down()
            sprite += e.get_effect()
    
    print(signal_strength)