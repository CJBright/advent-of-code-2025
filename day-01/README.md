# Day 1: Secret Entrance

Today's puzzle involved simulating a rotary safe dial numbered from 0 to 99. 
The dial began at a given starting position and was rotated according to a sequence of instructions detailing direction and distance rotated.

## Part 1

Part 1 asked for the number of times the dial ends on position 0 after each instruction.

**Approach**
- Set the initial state to the provided number.
- Parse the input into a series of instructions by parsing along newline chars.
- Extract each instruction into magnitude and direction components by taking slices on the line.
- Add or subtract the rotation's magnitude from the current position according to its direction. 
- Use a recurring function to handle rotations over 100 clicks.
- Update a tracking counter whenever the end position was at 0.

**Notes**
- The sequence overflow recurring function was replaced with a more optimal modulo and floor calculations within Part 2.


## Part 2

Part 2 asked for the number of times the dial was at the number 0 at any point during the movements.

**Approach**
- Set the initial state to the provided number.
- Parse the input data into a series of instructions by parsing along newline chars.
- Parse instructions into magnitude and direction components by taking slices on the line.
- Determine the number of full rotations (100-steps) within the magnitude and find the remainder steps for the movement.
- Each full rotation contributes exactly one zero-crossing.
- For the remainder, determine if the movement crosses 0 based on start position and direction.
- Wrap the final position into the valid range for the next step.

## Notes
When rotating left from a position of 0, the remainder of rotation should not count as crossing 0 - this edge case is accounted for by considering the current position before movement. 
