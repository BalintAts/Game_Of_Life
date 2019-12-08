## Game_Of_Life
This is a simple implementation of Conway's Game of Life. 

## Game of Life is a cellular automaton.
The default rules are:
- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

You can change the rules by modifying the rules.txt like this:
- The first column is the number of the surrounding cells in question.
- The second column is the surrounding cells state.
- The third column is the central cell's state. 
