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
  Created on Tue Dec 13 09:40:59 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Find shared element of 2 strings.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename
import string

#-- L O G I C -----------------------------------------------------------------

class Rucksack:
    """Rucksack storing a string."""
    
    def __init__(self, contents : str, compartments=2):
        self.contents = contents
    
    def __repr__(self) -> str:
        """Get a string representation of the Rucksack."""
        return f'Rucksack({self.contents})'
    
    def split_contents(self, contents : str) -> tuple(str, str):
        """Split the content string in 2 equal halfs."""
        half = len(contents)//2
        return (contents[:half], contents[half:])
    
    def get_intersection(self, contents : tuple[str, str]):
        """Get the shared character of 2 strings."""
        unique_contents = (set(content) for content in contents)
        intersection_set = set.intersection(*unique_contents)
        return str(*intersection_set)
    
    def get_score(self, intersection : str):
        """Score letters alphabetically with lowercase first."""
        alphabet = string.ascii_lowercase
        if intersection.islower():
            return 1 + alphabet.index(intersection)
        else:
            return 27 + alphabet.index(intersection.lower())

#-- M A I N   L O O P ---------------------------------------------------------

if __name__ == '__main__':
    current_score = 0
    for element in read_data_generator(get_basename(__file__)):
        r = Rucksack(element)
        contents = r.split_contents(element)
        intersection = r.get_intersection(contents)
        score = r.get_score(intersection)
        current_score += score
        
    print(current_score)