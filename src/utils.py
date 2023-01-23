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
  Created on Mon Dec 12 20:52:05 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  General utility functions for reading in files.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

import os

def get_basename(file):
    """Get "dayXX.txt" from a file named "dayXX_YY.py"."""
    script_base = os.path.splitext(os.path.basename(file))[0]
    return os.path.join('..\data', f'{script_base[:-3]}.txt')

def read_data(file):
    """Read the whole file in memory."""
    with open(os.path.join('..\data', f'{file}.txt')) as f:
        return f.read()
    
def read_data_generator(file, start=0, strip=False):
    """Read lines from any starting point in the file and optionally strip them."""
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            if i >= start:
                yield line if not strip else line.strip()