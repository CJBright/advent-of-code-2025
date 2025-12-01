import logging
logging.basicConfig(level=logging.INFO)

def read_file(day, kind):
    filename = f"day-{day:02d}/{kind}.txt"
    with open(filename) as f:
        return f.read().strip()

def apply_overflow(current_pos):
    # Account for overflow of neighbouring values 0 and 99.
    if current_pos > 99:
        current_pos -= 100 # 100 -> 00 
    elif current_pos < 0:
        current_pos += 100 # -1 -> 99
    
    if current_pos > 99 or current_pos < 0:
        return apply_overflow(current_pos)
    
    return current_pos

""" 
PART 1

Tracking a spinning safe dial - Numbered 0 - 99.
Input is a list of rotations - with direction and magnitude of clicks.
Magnitudes may be any size.

Steps:
    1. Set the initial dial position at 50.
    2. Load the input and iterate over each instruction. 
    3. Split each instruction into direction and magnitude.
    4. Apply each instruction to update the dial's position.
    5. Account for bi-directional overflow between 0 and 99 values.
    6. Count the number of times the dial is at 0 after each step.
"""

def part_1(kind="input"):
    START_POS = 50
    current_pos = START_POS
    zeros_count = 0
    logging.debug(f"Starting position: {current_pos}.\n")

    data = read_file(1, kind)
    lines = data.split()
    for instruction in lines:
        direction = instruction[0]
        magnitude = int(instruction[1:])
        
        if direction == "L":
            current_pos -= magnitude
        else:
            current_pos += magnitude
        logging.debug(instruction)
        logging.debug(f"After instruction position: {current_pos}.")
        current_pos = apply_overflow(current_pos)
        logging.debug(f"After correction position: {current_pos}.\n")
        if current_pos == 0:
            zeros_count += 1
    logging.info(f"Final zeros count: {zeros_count}.")

"""
PART 2

Similar setup as Part 1, however...
Now we count how many times the dial points at 00 at all, even in passing.

Steps.
    1. Set the initial dial position at 50.
    2. Load the input and iterate over each instruction. 
    3. Split each instruction into direction and magnitude.
    4. If the magnitude is large > 100 calculate the number of full turns.
    5. Assess if the remaining magnitude will pass the 00 position.
    6. Update the dial's final position for the instruction.
    7. Update the total count for passing the 00 position.
"""

def part_2(kind="input"):
    START_POS = 50
    current_pos = START_POS
    zeros_count = 0
    logging.debug(f"Starting position: {current_pos}.\n")

    data = read_file(1, kind)
    lines = data.split()
    for instruction in lines:
        direction = instruction[0]
        magnitude = int(instruction[1:])

        full_turns = magnitude // 100
        zeros_count += full_turns

        remainder = magnitude % 100
        if direction == "L":
            if current_pos > 0 and remainder >= current_pos:
                zeros_count += 1
            current_pos -= remainder
        elif direction == "R":
            if remainder >= (100 - current_pos):
                zeros_count += 1
            current_pos += remainder

        logging.debug(instruction)
        logging.debug(f"Instruction end position: {current_pos}.")
        current_pos = apply_overflow(current_pos)
        logging.debug(f"After correction position: {current_pos}.\n")
        logging.debug(f"Current zeros count: {zeros_count}.\n")
    
    logging.info(f"Total zeros count: {zeros_count}.")

if __name__ == "__main__":
    part_1("example")
    part_1()
    part_2("example")
    part_2()
