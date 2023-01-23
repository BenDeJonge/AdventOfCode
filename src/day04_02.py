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
  Created on Wed Dec 14 11:21:20 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Check if two ranges overlap with one another.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename
from day04_01 import encompassing_ranges, get_ints_from_str

#-- L O G I C -----------------------------------------------------------------

def overlapping_ranges(r1 : tuple[int,int], r2 : tuple[int,int]) -> bool:
    """Check if r1 overlaps with r2."""
    low, hi = r2
    return any( num in range(low, hi+1) for num in r1 ) or encompassing_ranges(r2, r1)
    
#-- M A I N   L O O P ---------------------------------------------------------

if __name__ == '__main__':
    count = 0
    for element in read_data_generator(get_basename(__file__)):
        numbers = get_ints_from_str(element)
        r1, r2 = tuple(numbers[:2]), tuple(numbers[2:])
        
        if overlapping_ranges(r1, r2):
            count += 1
            
    print(count)