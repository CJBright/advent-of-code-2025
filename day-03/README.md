# Day 3: Lobby

## Part 1

This day's task showed rows of battery banks.
Each battery has a joltage value.
2 batteries per bank could be made active to produce a combined joltage.
Joltages were combined with concatenation from left to right (2 + 3 = 23).
Batteries could not be rearranged.
Part 1 asked for the largest joltage from 2 batteries from each bank.

**Approach**
- Split the input data into individual banks.
- Split each bank into an array of batteries.
- Search for the largest pairing of batteries.<br>
    The largest number will occur by finding the largest 10s value.<br>
    However, at least 1 battery must remain to the right for the 1s value.
    
    - Search n-1 positions in the array for the largest value of battery 1.<br>
        Where there are multiple, equal matches, assign the first instance<br>
        This allows more choices for an optimal value of battery 2.
    - From (battery 1's position + 1) to the nth position, search for the largest number again.
    - Concatenate the joltage values and store in an array.
- Sum all stored bank joltages.

## Part 2

In Part 2, there were 12 batteries to enable, following the same rules.
The methodology was the same as before:
- Assign the largest numbers to the first batteries in order.
- Ensure there are enough batteries in the bank for the remaining slots.

**Approach**
- Split the input into individual banks.
- Create a loop to assign 12 numbers.
- Scan the array for the largest value.
- Do not check array values if there are not enough spaces for other batteries.
- Repeat until all values of X are assigned.
- Concatenate the joltage values and store in an array.
- Sum all stored bank joltages.