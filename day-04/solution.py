import logging
logging.basicConfig(level=logging.INFO)

def read_file(day, kind):
    filename = f"day-{day:02d}/{kind}.txt"
    with open(filename) as f:
        return f.read().strip()

"""
PART 1

Provided a map of rolls of paper.
Rolls with <4 adjacent rolls in the 8 positions can be accessed.
Search for accessible positions and sum the total number.

Steps:
- Define empty space as "." and rolls as "@".
- Consider walls as impassable.
- Go through the map item wise (for row, for col).
- If the checked item is empty, skip it.
- If the checked item is a roll, check its 8 neighbours.
- Search i, j value pair combinations -1, 0, +1 of the current value.
- Track the number of rolls within the 8 directions of the current roll.
- If rolls >= 4, continue to next positions.
- Else add to the tracker sum.
"""

def part_1(kind="input"):
    data = read_file(4, kind).split()
    accessible_rolls = 0
    
    # Go piecewise through the map.
    for row_idx in range(len(data)):
        for col_idx in range(len(data[0])):

            # Skip empty items
            if data[row_idx][col_idx] == ".":
                continue
            adj_rolls = 0
            
            for row_aug in range (-1, 2):
                # Check the 8 adjacent cells - augmenting rows -1, 0, +1
                if row_idx + row_aug < 0 or row_idx + row_aug > (len(data) - 1):
                    # Skip out of bounds entries
                    continue
                for col_aug in range(-1, 2):
                    # Check the 8 adjacent cells - augmenting columns -1, 0, +1
                    if col_idx + col_aug < 0 or col_idx + col_aug > (len(data[0]) - 1):
                        # Skip out of bounds entries
                        continue
                    if col_aug == 0 and row_aug == 0:
                        # Don't count the item being checked
                        continue
                    if data[row_idx + row_aug][col_idx + col_aug] == "@":
                        # Add the number of adjacent items
                        adj_rolls += 1
            # Add to sum of they are accessible.
            if adj_rolls < 4 :
                accessible_rolls += 1
    print(f"ACCESSIBLE TOTAL: {accessible_rolls}")


"""
PART 2

After scanning for the accessible rolls of paper, they are removed.
Repeat the process until no more rolls are accessible.
Sum the total number of rolls that were removed.

Steps:
- Define empty space as "." and rolls as "@".
- Consider walls as impassable.
- Go through the map item wise (for row, for col).
- If the checked item is empty, skip it.
- If the checked item is a roll, check its 8 neighbours.
- Search i, j value pair combinations -1, 0, +1 of the current value.
- Track the number of rolls within the 8 directions of the current roll.
- If rolls >= 4, continue to next positions.
- Else add to the tracker sum track and index to be altered.
- At the end of the scan alter all indices and repeat until no indices need altering.
"""

def part_2(kind="input"):

    def alter_indices(data, idx_list):
        # Replaces rolls with empty space when removed.
        for idx in idx_list:
            row, col = idx[0], idx[1]
            data[row][col] = "."
        return data
    
    def find_access(map):
        accessible_rolls = 0
        alter_idx = []
        for row_idx in range(len(map)):
            for col_idx in range(len(map[0])):
                adj_rolls = 0
                if map[row_idx][col_idx] == ".":   # Skip empty items
                    continue
                for row_aug in range (-1, 2):   # Augmenting rows
                    if row_idx + row_aug < 0 or row_idx + row_aug > (len(map) - 1):    # Skip out of bounds
                        continue
                    for col_aug in range(-1, 2):    # Augmenting columns
                        if col_idx + col_aug < 0 or col_idx + col_aug > (len(map[0]) - 1): # Skip out of bounds
                            continue
                        if col_aug == 0 and row_aug == 0:   # Don't count the item being checked
                            continue
                        if map[row_idx + row_aug][col_idx + col_aug] == "@": # Add the number of adjacent items
                            adj_rolls += 1
                if adj_rolls < 4 :  # Add to sum of they are accessible.
                    accessible_rolls += 1
                    alter_idx.append((row_idx, col_idx))
        
        # Loop until no loop has indices to change
        if alter_idx != []:
            map = alter_indices(map, alter_idx)
            accessible_rolls += find_access(map)
        return accessible_rolls

    data = read_file(4, kind).split()
    data = [list(row) for row in data]
    total_rolls = find_access(data)
    print(f"ACCESSIBLE TOTAL: {total_rolls}")


if __name__ == "__main__":
    part_1("example")
    part_1()
    part_2("example")
    part_2()