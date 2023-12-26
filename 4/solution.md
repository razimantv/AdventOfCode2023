# Problem 4

[Problem link](https://adventofcode.com/2023/day/4)

## Part 1

**Problem Statement**: Given two lists of numbers, find how many elements in the first are present in the second.

**Solution**. Treat them as sets and take their intersection.

[**Code**](1.py)

## Part 2

**Problem Statement**: You are given `n` cards. If the number on the `i`th card is `x`, you get an extra card of each of types `i+1` to `i+x`. Each of those cards can then give you extra cards of the following types and so on. How many cards do you end up with? 

**Solution**: This was the first *nontrivial* problem of the set. If we scan through the list of cards, how do we make the updates to the remaining cards efficiently? The first optimisation is to group cards of the same type together. Find out how many cards we have of each type, and process all of them efficiently (If we have `y` copies of card `i` with value `x`, instead of updating the following `x` cards `y` times, increase the values by `y` in one pass. This turns an exponential solution into a polynomial one.

There is an extra speedup possible by using prefix sums. By adding `y` to the count of the `i+1`th card and subtracting it from that of the `i+x+1`th card and taking prefix sums, we can find the correct number of cards for all the kinds in linear time instead of quadratic. For more problems using this trick, check the ["Prefix sums for range updates"](https://github.com/razimantv/leetcode-solutions#for-range-updates) tag in my [Leetcode solution repository](https://github.com/razimantv/leetcode-solutions).

[**Code**](2.py)

