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
  Created on Wed Dec 14 12:50:41 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Parse instructions. Move crates while preserving order.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename
from day04_01 import get_ints_from_str
from day05_01 import parse_stacks

#-- M A I N   L O O P ---------------------------------------------------------

# Read the stacks from the top of the file.
stacks, stop_line = parse_stacks( read_data_generator(get_basename(__file__)) )

# Read the instructions from the bottom. Move crates. Create message.
for line in read_data_generator(get_basename(__file__), start=stop_line+1):
    n_crates, source, destination = get_ints_from_str(line)
    stacks[source].move_to(stacks[destination], number=n_crates, swap_order=False)

msg = ''
for stack in stacks.values():
    msg += stack.get_top()