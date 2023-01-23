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
  Created on Sat Dec 17 17:36:56 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Find elements in array with only smaller neighbors along any axis.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename
import numpy as np

#-- L O G I C -----------------------------------------------------------------

def parse_row(row) -> list[int, ...]:
    """Return a list of integers from a string of integers."""
    return [int(i) for i in row]
    
def is_largest(array : np.ndarray, val : int) -> bool:
    """Check if a value is larger than any value in an array."""
    return val > array.max()

#-- M A  I N   L O O P --------------------------------------------------------

# Assembling forrest.
data = read_data_generator(get_basename(__file__), strip=True)
forrest = np.array([int(tree) for tree in next(data)])
for line in data:
    treerow = parse_row(line)
    forrest = np.vstack( (forrest, treerow) )

# Outside trees are visible everywhere.
visible = 2 * forrest.shape[0] + 2 * forrest.shape[1] - 4
best_scenic_score = 0
# Define 4 directions of a tree.
for row in range(1, forrest.shape[0] - 1):
    for col in range(1, forrest.shape[1] - 1):
        tree = forrest[row][col]
        
        left = forrest[row][:col]
        right = forrest[row][col+1:]
        top = forrest[:row, col]
        bottom = forrest[row+1:, col]
        
        directions = (left[::-1], right, top[::-1], bottom)
                
        # If the tree is visible from any direction, count it.
        if any( (is_largest(direction, tree) for direction in directions) ):
            visible += 1
            # Count how many trees are lower in any direction from the trees perspective.
            scenic_scores = []
            for direction in directions:
                score = 1
                for neighbor in direction[:-1]:
                    if neighbor < tree:
                        score += 1
                    else:
                        break
                scenic_scores.append(score)
                
            scenic_score = np.prod(scenic_scores)
            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score

print(visible)                     
print(best_scenic_score)