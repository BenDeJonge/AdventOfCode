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
  Created on Sat Dec 17 17:17:51 2022
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
from day07_01 import FileTreeParser, File
from math import inf

#-- C O N S T A N T S ---------------------------------------------------------

TOPLEVEL = ('/', )
NEEDED_SPACE = 30_000_000
TOTAL_SPACE = 70_000_000

#-- M A I N   L O O P ---------------------------------------------------------

ftp = FileTreeParser()
dirs = {}

# Looping over all instructions.
for line in read_data_generator(get_basename(__file__), strip=True):
    file = ftp.parse_instruction(line)
    # Instruction contains a file that passes its size up along all directories.
    if file:
        affected, size = file.propagate_size_up()
        for path in affected:
            if not path in dirs:
                dirs[path] = size
            else:
                dirs[path] += size

# Get the minimum size to remove.
current_free = TOTAL_SPACE - dirs[TOPLEVEL]
target_size = NEEDED_SPACE - current_free
# Current optimal folder.
current_best = File((TOPLEVEL,), inf)
# Looping over all folders and checking if above target and below current best.
for folder, size in dirs.items():
    if current_best.size > size >= target_size:
        current_best = File(folder, size)

print(current_best.size)