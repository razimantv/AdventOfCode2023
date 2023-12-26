# Problem 1

[Problem link](https://adventofcode.com/2023/day/1)

## Part 1

**Problem Statement**: Find the first and last occurrence of a digit in each line.

**Solution**: Scan through each line and check whether each character is a digit. 

[**Code**](1.py)

## Part 2

**Problem Statement**: Same as above, but now some digits are spelled out in words.

**Solution**: An efficient solution would have been to make a single pass through each line, looking for substring matches for each digit/word. As we didn't have such strict time constraints here, I just ran `find()` twice for each digit and word - once in the forward direction and once backward.

[**Code**](2.py)

