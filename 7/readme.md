# Problem 7

[Problem link](https://adventofcode.com/2023/day/7)

## Part 1

**Problem Statement**: Find the ranking of poker hands.

**Solution**: Sort the hands by applying a counter to the values of the cards in the hand.

[**Code**](1.py)

## Part 2

**Problem Statement**: Repeat the same, if a Joker can be replaced by any card.

**Solution**: Replace the Jokers in the hand by every other card in the hand, and find the best ranking as above.

[**Code**](2.py)

