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
  Created on Fri Dec 16 13:06:33 2022
  Created by Ben De Jonge
╚═════════════════════════════════════════════════════════════════════════════╝


╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Purpose                                   ║
╠═════════════════════════════════════════════════════════════════════════════╣
  Parse shell instructions to find all directories below a given size.
╚═════════════════════════════════════════════════════════════════════════════╝

...............................................................................
"""

#-- I M P O R T S -------------------------------------------------------------

from utils import read_data_generator, get_basename

#-- C O N S T A N T S ---------------------------------------------------------

TOPLEVEL = '/'
MAXSIZE = 100_000

#-- L O G I C -----------------------------------------------------------------

class FileTreeParser:
    """Parse a file tree from root."""
    
    def __init__(self, path : tuple[str, ...] = (TOPLEVEL,)):
        self.path = path
       
    def __repr__(self) -> str:
        """Get a string representation of the FileTreeParser."""
        return f'FileTreeParser at {self.path}'
    
    def parse_instruction(self, line : str):
        """Return a File object based on the terminal instructions."""
        elements = line.split()
        # Getting instructions.
        if elements[0] == '$':
            # Changing directory.
            if elements[1] == 'cd':
                if elements[2] == TOPLEVEL:
                    self.path = self.to_toplevel()
                elif elements[2] == '..':
                    self.path = self.level_up()
                else:
                    self.path = self.level_down(elements[2])
        # Reading new file.
        elif elements[0].isnumeric():
             return File(self.path, int(elements[0]))
        # Any other instruction is irrelevant.
        return None

    def level_down(self, new_level) -> str:
        """Append a new_level to the current directory."""
        return self.path + (new_level,)
    
    def level_up(self) -> str:
        """Get a higher level directory."""
        if len(self.path) > 1:
            return self.path[:-1]
        else:
            raise FileNotFoundError(f'Already at toplevel "{TOPLEVEL}".')
        
    def to_toplevel(self):
        """Get the toplevel directory."""
        return (TOPLEVEL,)
    

class File:
    """A file with a path and size."""
    
    def __init__(self, path, size):
        self.path = path
        self.size = size
    
    def propagate_size_up(self):
        """Add the file size to all parent directories."""
        ftp = FileTreeParser(self.path)
        paths = [ftp.path]
        
        at_toplevel = False
        while not at_toplevel:
            try:
                new_path = ftp.level_up()
                ftp.path = new_path
                paths.append(new_path)
            except FileNotFoundError:
                at_toplevel = True
                return (paths, self.size)
                
    def __repr__(self) -> str:
        """Get a string representation of the File."""
        return f'File of size {self.size} at {self.path}'

#-- M A I N   L O O P ---------------------------------------------------------

if __name__ == '__main__':
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
    
    total_size = 0
    for folder, size in dirs.items():
        if size <= MAXSIZE:
            total_size += size
            
    print(total_size)