# Day 2: Gift Shop

## Part 1

Part 1 provided a series of product ID ranges.
Each range provided the IDs bounding the range (e.g. 101-156).
The task was to identify invalid product IDs within each range.
An invalid ID was described by a repeating unit appearing exactly two times.
Any leading zeros in an ID are not considered part of the ID.

**Approach**
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

## Part 2

Part 2 expanded the challenge to identify IDs comprised a repeating unit appearing 
any number of times.

**Approach**
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

**Notes**
In cases where a number has multiple repeating units, you must break the assessment 
to prevent multiple assignments to the matched ID array.
e.g. 222222 is:
    6x repeat of '2'.
    3x repeat of '22'.
    2x repeat of '222'.