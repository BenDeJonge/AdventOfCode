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
  Created on Tue Dec 13 10:52:16 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Group multiple strings together and find their shared element.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename
from day03_01 import Rucksack

#-- C O N S T A N T S ---------------------------------------------------------

current_score = 0
contents = []
max_group_size = 3
r = Rucksack('')

#-- M A I N   L O O P ---------------------------------------------------------

# Add elements until the group is full. Find the common element. Score it.
for element in read_data_generator(get_basename(__file__)):
    contents.append(element.strip())
    if len(contents) == max_group_size:
        intersection = r.get_intersection(contents)
        score = r.get_score(intersection)
        current_score += score
        
        contents = []
    
print(current_score)