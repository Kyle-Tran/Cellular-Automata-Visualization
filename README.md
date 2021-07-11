# Cellular Automata Visualization

[Cellular Automata](https://en.wikipedia.org/wiki/Cellular_automaton) on a 2D lattice.

Clone project using:

    git clone https://github.com/Kyle-Tran/Cellular-Automata-Visualization.git
    cd Cellular-Automata-Visualization

Run project using

    python project/main.py

and select parameters in console.

## Requirements
- Python 3.x
- Pygame
- Numpy

## Individual Modes

### [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

#### Rules:
- Any live cell with two or three live neighbors survives.
- Any dead cell with three live neighbors becomes a live cell.
- All other live cells die in the next generation.
- Similarly, all other dead cells stay dead.

#### Controls:
- **Left Click**: Change cell state (live to dead/vice versa)
- **Right Click**: Iterate through single generation
- **Spacebar**: Iterate continuously through generations
- **Ctrl + R**: Reset field
- **Ctrl + T**: Randomize field

#### Recommended Options (Edit in *main.py*):

- ***percentRandom***: Change percentage of cells that spawn live upon randomizing field
  - Recommend value between 0.1-0.5
- ***scalar***: Scales GUI down by factor of *scalar* based on monitor resolution
  - Recommend value between 10-20 for powerful CPU otherwise 30-60
- ***fps***: Changes speed between continuous generations 
  - Recommend value of 60 as default and 1-10 to see generations slowly
- ***conway_colors***: Array of colors for dead and live cells
  - [dead color, live color]
  - Recommend using default [white, duke_blue] or [white, black]
 ---   
### [Multi-state Cellular Automata](https://en.wikipedia.org/wiki/Cellular_automaton)

#### Rules:
- Generalized rock, paper, scissors rules (Ternary system)
    - Quinary system based on [rock, paper, scissors, lizard, spock rules](https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock)
- Cell converted if it has more than 2 neighbors that beats it.

#### Controls:
- **Left Click + 1,2,...,5 for Rock,Paper,...,Spock**: Change cell color
- **Right Click**: Iterate through single generation
- **Spacebar**: Iterate continuously through generations
- **Ctrl + R**: Reset field
- **Ctrl + T**: Randomize field
  
#### Recommended Options (Edit in *main.py*):

- ***scalar***: Scales GUI down by factor of *scalar* based on monitor resolution
  - Recommend value between 10-20 for powerful CPU otherwise 30-60
- ***fps***: Changes speed between continuous generations 
  - Recommend value of 60 as default and 1-10 to see generations slowly
- ***rps_colors***: Array of colors for each element
  - [rock, paper, scissors, lizard, spock]
  - Must be of length 5
  - Recommend using default [p1, p2, p3, p4, p5]
---
### [Langton's Ant](https://en.wikipedia.org/wiki/Langton%27s_ant)
  Squares on a plane are colored variously either black or white. 
  We arbitrarily identify one square as the "ant" (denoted as red square). 
  The ant can travel in any of the four cardinal directions at each step it takes. 
  The "ant" moves according to given ruleset.


#### Rules: 
A simple naming scheme is used: 

For each of the successive colors, a letter "L" or "R" is used
to indicate whether a left or right turn should be taken. 
Langton's ant has the name "RL" in this naming scheme.
- **Default Rule 'RL'**:
  - At a white square, turn 90° clockwise, flip the color of the square, move forward one unit
  - At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit

#### Controls:
- **Left Click + Arrow Key (up, right, down, left)**: Places ant on field in given cardinal direction
  - up = North, right = East, down = South, left = West
  - Default direction is north (if arrow key is not pressed)
- **Right Click**: Iterate through single generation
- **Spacebar**: Iterate continuously through generations
- **Ctrl + R**: Reset field 

#### Recommended Options (Edit in *main.py*):
- ***scalar***: Scales GUI down by factor of *scalar* based on monitor resolution
  - Recommend value between 1-10
- ***langton_rules***: String for rule-set for ant
  - Langton's ant is equivalent to 'RL'
- ***langton_colors***: Array of colors associated for each rule
  - e.g. *langton_rules* = 'RL', *langton_colors* = [black, white]
  - default implementation is one random RGB color for each rule
  - REQUIRED: len(langton_rules) == len(langton_colors)
 

#### Known Issues:
- Going full screen causes screen to go black
  - A temporary fix is to reset entire field (Ctrl + R)

---
## Neighborhoods
Neighbors are based upon a [Moore neighbourhood](https://en.wikipedia.org/wiki/Moore_neighborhood). 

## OTHER
Add your own colors below ***"&ast;&ast;&ast; COLORS &ast;&ast;&ast;"*** in *main.py*
   - Takes form of three-tuple RGB color: (r, g, b)