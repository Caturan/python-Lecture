"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.
If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
"""

"""
To solve this problem, you can model it as finding the maximum probability path in a graph. Since it's an undirected weighted graph, where the weights are probabilities,
 you can use a modified version of Dijkstra's algorithm. 
Instead of summing up the weights (like in the shortest path problem), you'll multiply the probabilities along the path. 
 However, because multiplying small probabilities can be tricky, we'll work with the logarithm of the probabilities to avoid floating-point precision issues.

Here's the step-by-step approach:
Graph Representation: Represent the graph as an adjacency list where each node has a list of connected nodes along with the corresponding success probability.

Dijkstra's Algorithm:

Use a priority queue (max-heap) to keep track of the node with the maximum probability found so far.
Start from the start node, initialize its probability to 1 (since the probability of starting at the start node is 100%).
For each node, explore its neighbors, calculate the probability of reaching the neighbor through the current node, and update the neighbor's probability if this path is better.
Continue until you reach the end node or until all possible paths are explored.
Edge Cases:

If the start and end nodes are the same, the result is 1.
If there is no path from start to end, return 0.
"""
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Step 1: Create the adjacency list
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        # Step 2: Dijkstra's algorithm using max-heap
        max_heap = [(-1.0, start_node)]  # Use negative because heapq in Python is a min-heap by default
        probabilities = [0.0] * n
        probabilities[start_node] = 1.0
        
        while max_heap:
            current_prob, node = heapq.heappop(max_heap)
            current_prob = -current_prob  # Convert back to positive
            
            if node == end_node:
                return current_prob
            
            for neighbor, prob in graph[node]:
                new_prob = current_prob * prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        return 0.0

