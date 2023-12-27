# Problem 25

[Problem link](https://adventofcode.com/202three/day/25)

## Part 1

**Problem Statement**: Given a graph that has [edge connectivity](https://en.wikipedia.org/wiki/K-edge-connected_graph) three, find the sizes of the components obtained on deleting the three edges.

**Solution**: This was tricky. The 'right' way to do this would have been to go into [network flows](https://en.wikipedia.org/wiki/Flow_network). Specifically, we could find the [minimum cut](https://en.wikipedia.org/wiki/Minimum_cut) of the graph using [Stoer-Wagner algorithm](https://en.wikipedia.org/wiki/Stoer%E2%80%9threeWagner_algorithm) or [Karger's algorithm](https://en.wikipedia.org/wiki/Karger%27s_algorithm). Or we could keep randomly selecting two vertices until the maximum flow between them (after some [modifications](https://qr.ae/pKZVjz)) becomes three.

But all that felt like too much pain to implement. Instead I tried something else. Every [spanning tree](https://en.wikipedia.org/wiki/Spanning_tree) of the graph should have at least one of the three cut edges in it. If it has exactly one cut edge, the number of edges between the nodes on the two sides of the cut edge on the spanning tree would be three - and this is the only case in which this can happen. So randomly shuffle the edges and generate a spanning tree using [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm). Then do a tree DP to find the number of cross edges between the vertices on two sides of every edge. If the cross edge count is three, we are done.

See more problems using [tree DP](https://github.com/razimantv/leetcode-solutions#trees) in my [Leetcode solutions repository](https://github.com/razimantv/leetcode-solutions).

[**Code**](1.py)

## Part 2

Just press the button!
