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
  Created on Tue Dec 20 13:55:51 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Multiple tail Knots follow the head Knot.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename
from day09_01 import Knot, get_moves, plot_knots

#-- C O N S T A N T S ---------------------------------------------------------

n_knots = 10

#-- M A I N   L O O P ---------------------------------------------------------

knots = [ Knot(0,0, None,None) for i in range(n_knots) ]
head = knots[0]
tail = knots[-1]
    
positions = {tail.position,}
for line in read_data_generator(get_basename(__file__), strip=True):
    direction, number = get_moves(line)
    for i in range(number):
        head.move(direction)
        for j, knot in enumerate(knots[1:]):
            previous = knots[j]
            knot.follow(previous)
            if knot == tail:
                positions.add(knot.position)
    # fig, ax = plot_knots(knots, title=f'Position after {line}', xlim=(-16,16), ylim=(-6,16))
    
print(len(positions))