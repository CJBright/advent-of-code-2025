import logging
logging.basicConfig(level=logging.INFO)

def read_file(day, kind):
    filename = f"day-{day:02d}/{kind}.txt"
    with open(filename) as f:
        return f.read().strip()

"""
PART 1

Part 1 provided a series of product ID ranges.
Each range provided the IDs bounding the range (e.g. 101-156).
The task was to identify invalid product IDs within each range.
An invalid ID was described by a repeating unit appearing exactly two times.
Any leading zeros in an ID are not considered part of the ID.

STEPS:
- Load in the input file.
- Split the file so that each ID range was a unique input to be iterated over.
- Split each range into its upper and lower bounds.
- Consider edge cases where the range was given in reverse order.
- Create an array of all IDs within the range.
- Iterate over each range to assess repeating units.
- Remove leading zeros from the ID.
- Ignore odd length IDs as these could not be made by a 2x repeating unit.
- Slice even length IDs in half and assess equality of 1st half x2 vs whole ID.
- Store any cases where this is true.
- Sum the stored IDs to complete the challenge. 
"""

def part_1(kind="input"):
    data = read_file(2, kind).split(",")
    invalid_ids = []

    for id_range in data:
        # Extract list of ID values in the range
        lower, upper = id_range.split("-")
        lower, upper = int(lower), int(upper)
        step = 1 if upper >= lower else -1
        list_augment = 1 if upper >= lower else -1
        id_values = list(range(lower, upper + list_augment, step))
        logging.debug(id_values)

        for id_single in id_values:
            # Process ID values
            id_single = int(str(id_single).lstrip("0")) # Remove any leading 0s.
            if len(str(id_single)) % 2 != 0: continue # Skip odd length IDs
            if str(id_single)[:(int(len(str(id_single)) / 2))] * 2 == str(id_single):
                logging.debug("Match", id_single)
                invalid_ids.append(id_single)
    
    logging.debug(invalid_ids)
    logging.info(sum(invalid_ids))

"""
PART 2

Given a series of ID ranges indicated by the lowest and largest values.
Expand each range and identify IDs which are made of some repeating pattern.
Ignore any leading zeros on ID numbers.

STEPS:
- Load in the input file.
- Split the file so that each ID range was a unique input to be iterated over.
- Split each range into its upper and lower bounds.
- Consider edge cases where the range was given in reverse order.
- Create an array of all IDs within the range.
- Iterate over each range to assess repeating units.
- Remove leading zeros from the ID.
- Break each ID into sections of its self (halves, thirds, quarters, etc.)
    (done by taking the value of division where the result is an integer)
- Assess [section * repeat amount] against the whole ID for equality.
    (If any match is found stop assessing)
- Store any cases where this is true.
- Sum the stored IDs to complete the challenge. 
"""

def part_2(kind="input"):
    data = read_file(2, kind).split(",")
    invalid_ids = []

    for id_range in data:
        # Extract list of ID values in the range
        lower, upper = id_range.split("-")
        lower, upper = int(lower), int(upper)
        step = 1 if upper >= lower else -1
        list_augment = 1 if upper >= lower else -1
        id_values = list(range(lower, upper + list_augment, step))
        logging.debug(id_values)

        for id_single in id_values:
            # Process ID values
            id_single = int(str(id_single).lstrip("0")) # Remove any leading 0s.            
            max_divisions = len(str(id_single))
            for i in range(max_divisions):
                if len(str(id_single)) % (i + 1) == 0 and int(max_divisions / (i + 1)) > 1:
                    if str(id_single)[:i + 1] * int(max_divisions / (i + 1)) == str(id_single):
                        logging.debug("Match", id_single)
                        invalid_ids.append(id_single)
                        break # Prevent a number matching in multiple breaks e.g. 2222
    
    logging.debug(invalid_ids)
    logging.info(sum(invalid_ids))


if __name__ == "__main__":
    part_1("example")
    part_1()
    part_2("example")
    part_2()
