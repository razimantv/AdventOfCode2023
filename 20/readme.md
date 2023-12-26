# Problem 20

[Problem link](https://adventofcode.com/2023/day/20)

## Part 1

**Problem Statement**: Given a network with 2 kinds of pulses (high, low) and 2 kinds of nodes:

1. Flip-flops which have an on-off state. They ignore high pulses and on low pulses, change their state and forward high/low pulses depending on their state
2. Conjunction modules, on receiving a pulse, forward a low pulse if the last received pulse from all its neighbours were high pulses and a high pulse otherwise.

Find the total number of low pulses sent in the network if a broadcaster sends low pulses to its neighbours a 1000 times?

**Solution**: Simulate the process, bookkeeping the last pulse each node received from all its neighbours.

[**Code**](1.py)

## Part 2

**Problem Statement**: Find how many broadcast pulses are required before a given node first receives a low pulse?

**Solution**: This one required us to inspect the input. Turned out that the target node `rx` received pulses only from a conjunction node `ll`, which in turn received pulses from 4 other conjunction nodes. So the question was about when all of these nodes would send high pulses to `ll`. As in [Problem 8](../8/solution.md), a lot of complication was avoided by the fact that all these nodes sent high pulses at periodic intervals allowing us to take the LCM of the periods.

[**Code**](2.py)

