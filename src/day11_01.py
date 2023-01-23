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
  Created on Wed Dec 21 00:54:14 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

from utils import read_data_generator, get_basename
from day04_01 import get_ints_from_str
from numpy import prod

MONKEY_DICT = {}
WORRY_DECAY = 3
N_ROUNDS = 20

total_divisor = 1

class Monkey:
    
    @classmethod
    def parse_from_string(self, string):     
        monkey_dict = {'index'     : None,
                       'worries'   : None,
                       'operation' : None,
                       'operand'   : None,
                       'factor'    : None,
                       'divisor'   : None,
                       'partners'  : None}
        
        temp_partners = []

        elements = string.split('\n')
        for element in elements:
            if element.startswith('Monkey'):
                monkey_dict['index'] = get_ints_from_str(element)[0]
            elif element.startswith('  Starting items'):
                monkey_dict['worries'] = list(get_ints_from_str(element))
            elif element.startswith('  Operation'):
                try:
                    factor = get_ints_from_str(element)[0]
                
                    operations = {'+' : lambda x : x + factor,
                                  '-' : lambda x : x - factor,
                                  '*' : lambda x : x * factor,
                                  '/' : lambda x : x / factor}
                    
                    for symbol, operation in operations.items():
                        if symbol in element:
                            monkey_dict['operation'] = operation
                            monkey_dict['operand'] = symbol
                            monkey_dict['factor'] = factor
                            break
                except IndexError:
                    monkey_dict['operation'] = lambda x : x**2
            elif element.startswith('  Test'):
                monkey_dict['divisor'] = get_ints_from_str(element)[0]
            elif 'throw to monkey' in element:
                temp_partners.append(get_ints_from_str(element)[0])
        
        monkey_dict['partners'] = tuple(temp_partners)
        
        return monkey_dict['index'], Monkey(worries   = monkey_dict['worries'],
                                            operation = monkey_dict['operation'],
                                            operand   = monkey_dict['operand'],
                                            factor    = monkey_dict['factor'],
                                            divisor   = monkey_dict['divisor'],
                                            partners  = monkey_dict['partners'])
                
    def __init__(self, 
                 worries : list[int, ...] = [],
                 operation : callable = lambda x : x,
                 operand : str = '',
                 factor : int = 1,
                 divisor : int = 1,
                 partners : (int, int) = (0,1)
                 ):
        self.worries = worries
        self.operation = operation
        self._operand = operand
        self._factor = factor
        self.divisor = divisor
        self.partners = partners
        self.inspections = 0
        
    worry_decay : int = WORRY_DECAY

    def __repr__(self) -> str:
        return f''''Monkey(
    worries = {self.worries},
    operation = {self.operation},
    divisor = {self.divisor},
    partners = {self.partners}
    )'''

    def examine_items(self) -> list[int, ...]:
        self.worries = [ self.operation(worry) // Monkey.worry_decay
                        for worry in self.worries ]
    
    def throw_items(self):
        if not self.worries:
            return
        for worry in self.worries:
            self.inspections += 1
            if worry % self.divisor == 0:
                i_other = self.partners[0]
            else:
                i_other = self.partners[1]
            self.throw(worry, i_other)
        self.worries = []
        
    def throw(self, worry : int, i_other : int) -> None:
        MONKEY_DICT[i_other].worries.append(worry)

monkey_str = ''
start = 0
n_lines = 7


for i, line in enumerate( read_data_generator(get_basename(__file__)) ):
    monkey_str += line
    if (i + 2) % n_lines == 0:
        i, monkey = Monkey.parse_from_string(monkey_str)
        MONKEY_DICT[i] = monkey
        monkey_str = ''

# for monkey in MONKEY_DICT.values():
#     if monkey._operand == '*':
#         total_divisor *= monkey._factor

# Monkey.worry_decay = total_divisor

for run in range(N_ROUNDS):
    if run % 100 == 0:
        print(f'Run {run+1}/{N_ROUNDS}')
    for i, monkey in MONKEY_DICT.items():
        monkey.examine_items()
        monkey.throw_items()


inspections = sorted( [monkey.inspections for monkey in MONKEY_DICT.values()] )
print(prod(inspections[-2:]))