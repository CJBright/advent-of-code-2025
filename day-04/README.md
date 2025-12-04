# Day 4: Printing Department

## Part 1
In Part 1 we are provided with a map/grid of shelves with wrapping paper:
- Empty and full spaces are indicated differently.
- We are told to identify accessible wrapping paper.
- Wrapping paper is deemed accessible if there are <4 other wrapping papers in the 8 adjacent cells.

**Steps**
- To identify accessible cells I iterate through every cell on the map.
- I first check if the cell is empty (skip) or contains wrapping paper (process).
- When processing the cell, I augment the current index's row and column values by 1 to the adjacent cell's contents.
- I use an internal counter to keep track of the total number of adjacent wrapping papers.
- If the number is under the threshold a global accessible paper counter is increased, otherwise we move on to assess the next cell. 
- Consideration is given to the walls, such that they are bounded rather than looping.

## Part 2

Part 2 expands on this.
- The identified accessible papers are removed and the search is restarted. 
- This is repeated until no further wrapping papers may be removed.

**Steps**
- To tackle this I turned the searching code described before into a recurring function.
- When an accessible index is found it now updates the count but also tracks its position,.
- A new function is produced to augment any removed wrapping papers into empty cells. The input data is converted from a string to an array to support this.
- The sorting code continues to run until there no indices are found to augment, indicating no accessible positions and a complete puzzle.
