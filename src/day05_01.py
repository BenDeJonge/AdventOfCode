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
  Created on Wed Dec 14 11:45:15 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Parse instructions. Move crates without preserving order.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename
from day04_01 import get_ints_from_str

#-- L O G I C -----------------------------------------------------------------

class Stack:
    """A Stack of crates."""
    
    def __init__(self, elements : str):
        self.elements = elements
            
    def __iadd__(self, val : str) -> None:
        """Replace the Stack by adding a new element to the back."""
        self.elements += val
        return self
    
    def __add__(self, val : str) -> str:
        """Add a new element to the back of the Stack."""
        return self.elements + val
    
    def __repr__(self) -> str:
        """Return a string representation of the Stack."""
        return f'Stack({self.elements})'
    
    def move_to(self, other, number = 1, swap_order=False) -> None:
        """Update elements of 2 Stacks by moving the last elements between them."""
        if not swap_order:
            other += self.get_top(number)
        else:
            other += self.get_top(number)[::-1]
        self.elements = self.elements[:-number]
    
    def get_top(self, n=1) -> str:
        """Get the last elements of the stack."""
        return self.elements[-n:]
        
def parse_stacks(file : str) -> (dict[int:Stack, ...], int):
    """
    Parse a graphical represenation of Stacks from a file.

    Parameters
    ----------
    file : str
        DESCRIPTION.

    Returns
    -------
    stacks : dict[int:Stack, ...]
        A dictionary of index : stack key-value-pairs.
    i : int
        The line where the graphical representation stops in the file.
    """
    lines = []
    for i, line in enumerate(file):
        if line == '\n':
            break
        lines.append(line)

    stack_names = get_ints_from_str(lines[-1])
    stacks = { i : Stack('') for i in stack_names}
    stack_positions = [lines[-1].index(str(name)) for name in stack_names]
    
    for line in lines[-2::-1]:
        for name, position in zip(stack_names, stack_positions):
            letter = line[position]
            if letter.isalpha():
                stacks[name] += letter
    
    return stacks, i

#-- M A I N   L O O P ---------------------------------------------------------

# Read the stacks from the top of the file.
stacks, stop_line = parse_stacks( read_data_generator(get_basename(__file__)) )

# Read the instructions from the bottom. Move crates. Create message.
for line in read_data_generator(get_basename(__file__), start=stop_line+1):
    n_crates, source, destination = get_ints_from_str(line)
    stacks[source].move_to(stacks[destination], number=n_crates, swap_order=True)

msg = ''
for stack in stacks.values():
    msg += stack.get_top()
    
print(msg)