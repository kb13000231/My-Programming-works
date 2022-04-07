import queue
# e = no. of edges
# n = no. of nodes
# T = O(e) and S = O(n)


def breadthFirstSearch(graph, source):
    queue = [source]
    while len(queue) > 0:
        curr = queue.pop()
        print(curr)
        for neighbor in graph[curr]:
            queue.insert(0, neighbor)


def breadthFirstSearchopt(graph, source):
    q = queue.Queue()
    q.put(source)

    while q.qsize() > 0:
        curr = q.get()
        print(curr)
        for neighbor in graph[curr]:
            q.put(neighbor)


GRAPH = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    "e": [],
    'f': []
}

print('Naive:')
breadthFirstSearch(GRAPH, 'a')
print('Optimal:')
breadthFirstSearchopt(GRAPH, 'a')
