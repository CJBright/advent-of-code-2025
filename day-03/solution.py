import logging
logging.basicConfig(level=logging.INFO)

def read_file(day, kind):
    filename = f"day-{day:02d}/{kind}.txt"
    with open(filename) as f:
        return f.read().strip()

"""
PART 1

Each line in the input is a bank of batteries.
Each battery is labelled with their joltage value (1-9).
Turn on exactly 2 batteries to produce a concatenated joltage (2 + 4 = 24).
Concatenation is from left to right. 
Batteries can not be rearranged. 
Find the largest joltage for each bank.

Steps:
    - Split the input data into individual banks.
    - Split each bank into an array of batteries.
    - Search for the largest pairing in order.
        - Search the n-1 positions in the array for the largest number.
            (where multiple. take the first instance)
        - From that position onwards to n, search for the largest number again.
        - Concatenate the numerical values into a bank joltage and store.
        - Sum all bank joltages.
"""

def part_1(kind="input"):
    data = read_file(3, kind).split("\n")
    joltages = []
    for bank in data:
        bank = list(bank)
        battery_1 = bank[0]
        b_2_index = 1

        # Find largest value for battery_1 in index 0 to n-1
        for i in range(len(bank) - 2):
            if bank[i + 1] > battery_1:
                battery_1 = bank[i + 1]
                b_2_index = i + 2
        logging.debug(f"Battery_1 value: {battery_1}.")
        logging.debug(f"B_2_index value: {b_2_index}.")
        
        # Find largest value for battery_2 in index i+1 to n.
        battery_2 = bank[b_2_index]
        for j in range(b_2_index, (len(bank) - 1)):
            if bank[j + 1] > battery_2:
                battery_2 = bank[j + 1]
        logging.debug(f"Battery_2 value: {battery_2}.")

        # Append largest joltage to array.
        bank_joltage = int(str(battery_1) + str(battery_2))
        joltages.append(bank_joltage)
        logging.debug(f"Bank joltage value: {bank_joltage}.")
    
    # Return total
    logging.info(sum(joltages))


"""
PART 2

Turn on exactly 12 batteries within each bank to make the largest joltage.
Same premise as before, just much larger scale.

Similarly to before, to find the largest number you need to fill the numbers
from left to right with their largest values.
Find the largest value with at least 11 indices to its right.
Find the largest value with at least 10 indices to its right.
...
find the last, largest value.

Steps:
    - Split the input into individual banks.
    - Create a loop to assign 12 numbers spaces - X.
    - Scan the array for the largest value.
        - If there are at least X-1 indices remaining, assign the value.
        - If there are not, scan for a 1 smaller value.
    - Repeat until all values of X are assigned.
"""

def part_2(kind="input"):
    data = read_file(3, kind).split("\n")
    joltages = []
    for bank in data:
        bank = list(bank)
        bank_values = {}
        next_battery_index = 0

        for i in range(12):
            
            start_index = next_battery_index
            remaining_slots = 12 - (i + 1)
            max_index = len(bank) - remaining_slots - 1
            best_index = start_index

            for battery_index in range(start_index, max_index + 1):
                if bank[battery_index] > bank[best_index]:
                    best_index = battery_index

            bank_values[i] = bank[best_index]
            logging.debug(
                f"Battery {i}: chose {bank[best_index]} at index {best_index} "
                f"(range {start_index}-{max_index})"
            )

            # Next battery must start 1 place after newly assigned one
            next_battery_index = best_index + 1

        joltage_str = "".join(bank_values[i] for i in range(12))
        joltages.append(int(joltage_str))
        logging.debug(f"Joltages: {joltages}")

    logging.info(f"Total: {sum(joltages)}")

if __name__ == "__main__":
    part_1("example")
    part_1()
    part_2("example")
    part_2()