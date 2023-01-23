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
  Created on Mon Dec 19 16:00:23 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  One tail Knot follows a head Knot.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename
import numpy as np
import matplotlib.pyplot as plt

class Knot:
    """A knot in a rope with a current and previous position."""
    
    #-- D U N D E R   M E T H O D S -------------------------------------------
    def __init__(self, x, y, x_prev, y_prev, max_dist=2):
        self._x = x
        self._y = y
        self.max_dist = max_dist
        self._x_prev = x_prev
        self._y_prev = y_prev
        self.position = (self.x, self.y)
        self.position_prev = (self.x_prev, self.y_prev)
        
        
    def __repr__(self) -> str:
        """Get a string represenation of the Knot."""
        return f'Knot({self.x}, {self.y})'   
    
    
    def __sub__(self, other):
        """Subtract coordinates of 2 Knots."""
        return (self.x - other.x, self.y - other.y)
    
    #-- P R O P E R T I E S ---------------------------------------------------

    @property
    def position(self):
        """Property of position."""
        return self._position
    @position.setter
    def position(self, val):
        if all(isinstance(v, (int, float)) for v in val):
            self._position = val
            self.x, self.y = val
            
    @property
    def x(self):
        """Property of x-coordinate."""
        return self._x
    @x.setter
    def x(self, val):
        if isinstance(val, (int, float)):
            self._position = (val, self._y)
            self._x = val
            
    @property
    def y(self):
        """Property of x-coordinate."""
        return self._y
    @y.setter
    def y(self, val):
        if isinstance(val, (int, float)):
            self._position = (self._x, val)
            self._y = val
            
    @property
    def position_prev(self):
        """Property of previous position."""
        return self._position_prev
    @position_prev.setter
    def position_prev(self, val):
        if all(isinstance(v, (int, float)) for v in val):
            self._position_prev = val
            self._x_prev, self._y_prev = val
        if any(not v for v in val):
            self._position_prev = self.position
            self._x_prev, self._y_prev = self.position
            
    @property
    def x_prev(self):
        """Property of previous x-coordinate."""
        return self._x_prev
    @x_prev.setter
    def x_prev(self, val):
        if isinstance(val, (int, float)):
            self._position_prev = (val, self._y_prev)
            self._x_prev = val
            
    @property
    def y_prev(self):
        """Property of previous y-coordinate."""
        return self._y_prev
    @y_prev.setter
    def y_prev(self, val):
        if isinstance(val, (int, float)):
            self._position = (self._x_prev, val)
            self._y_prev = val
    
        
    #-- L O G I C -------------------------------------------------------------
    
    def get_distance(self, other) -> float:
        """Get the Euclidian distance between 2 Knots."""
        return ( (self.x - other.x)**2 + (self.y - other.y)**2 )**0.5
    
    
    def move(self, direction : str):
        """Move the Knot in any of 4 directions."""
        self.previous_position = self.position
        direction = direction.lower()
        if direction == 'up':
            self.y += 1
        elif direction == 'down':
            self.y -= 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
        self.position = (self.x, self.y)
    
    
    def follow(self, other):
        """Follow another Knot.
        
        Rules for gradients of self.(x,y) - other.(x,y):
            (0,0) : NONE
            (0,1) : NONE
            (0,2) : DOWN
            (1,2) : DOWN-LEFT
        And mirror appropriately for any other combination.
        """
        distance = self.get_distance(other)        

        # Horizontal and veritcal following.
        if distance == self.max_dist:
            # X needs changing.
            if self.x > other.x:
                self.move('left')
            elif self.x < other.x:
                self.move('right')
            # Y need changings.
            if self.y > other.y:
                self.move('down')
            elif self.y < other.y:
                self.move('up')
                
        # Diagonal following.
        elif distance > self.max_dist:
            # X needs changing.
            if self.x > other.x:
                self.move('left')
            else:
                self.move('right')
            # Y needs chaning.
            if self.y > other.y:
                self.move('down')
            else:
                self.move('up')
                
#------------------------------------------------------------------------------

def get_moves(line : str) -> (str, int):
    """Parse the input line to number of moves in a direction."""
    directions = {
        'R' : 'right',
        'L' : 'left',
        'U' : 'up',
        'D' : 'down'}
    direction, number = line.split()
    return directions[direction], int(number)

def plot_knots(knots : list[Knot,...], 
               title : str = 'Knots', xlabel : str = 'x', ylabel : str = 'y',
               xlim : tuple[int, int] = None, ylim : tuple[int, int] = None):
    """Plot a list of Knots."""
    xs, ys = [], []
    for knot in knots:
        xs.append(knot.x)
        ys.append(knot.y)
    colors = np.arange(len(knots))
    fig, ax = plt.subplots()
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)
    ax.scatter(xs, ys, c=colors)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(range(*xlim))
    ax.set_yticks(range(*ylim))
    ax.grid(True)
    return fig, ax

#-- M A I N   L O O P ---------------------------------------------------------

if __name__ == '__main__':
    
    head = Knot(0, 0, None, None)
    tail = Knot(0, 0, None, None)
    
    positions = {tail.position,}
    for line in read_data_generator(get_basename(__file__), strip=True):
        print(line)
        direction, number = get_moves(line)
        for i in range(number):
            head.move(direction)
            tail.follow(head)
            positions.add((tail.position))
        # fig, ax = plot_knots([head, tail], title=f'Position after {line}', xlim=(-16,16), ylim=(-6,16))
            
    print(len(positions))