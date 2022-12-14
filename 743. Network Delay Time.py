from typing import List
import collections
import heapq
''' This is an implementation of Djikstra's algorithm.'''
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    ''' defaultdict creates a dictionary which is very similar to a normal dict 
    creation, except that if youtry and accept a dict key that doesn't exist, 
    instead of giving you a keyerror it creates that key and inserts an empty 
    value (an empty list in this case) as its default value. '''
    edges = collections.defaultdict(list)
    for u, v, w in times:
        edges[u].append((v,w))

    minHeap = [(0,k)]
    visit = set() 
    t = 0
    while minHeap:
        # greedy selection of the shortest weight in the priority queue.
        w1, n1 = heapq.heappop(minHeap) 
        if n1 in visit:
            continue
        visit.add(n1)
        # keeping track of total time is an artefact required for the leetcode problem
        # and not part of the original algorithm.
        t = max(t, w1)

        for n2, w2 in edges[n1]:
            if n2 not in visit:
                # Adding weight of previous min weight path (w1) to the next smallest weight (w2)
                # into the priority queue allows us to compare all paths to find the shortest path.
                heapq.heappush(minHeap, (w2 + w1, n2))
    
    return t if len(visit) == n else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
print(networkDelayTime(times, 4, 2))
