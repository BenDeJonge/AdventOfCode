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
  Created on Fri Dec 16 12:55:21 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Find first instance of n unique characters in a string.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename

#-- C O N S T A N T S ---------------------------------------------------------

length = 14

#-- L O G I C -----------------------------------------------------------------

def get_index_unique_stretch(string : str,
                             length : int) -> int:
    """Find the first index that completes a unique stretch of given length."""
    for i in range(len(string) - length):
        stretch = string[i : i+length]
        if len(set(stretch)) == length:
            return i + length
    return -1

#-- M A I N   L O O P ---------------------------------------------------------

string = next( read_data_generator(get_basename(__file__)) )
print(get_index_unique_stretch(string, length))