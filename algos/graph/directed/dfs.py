# e = no. of edges
# n = no. of nodes
# T = O(e) and S = O(n)


def depthFirstSearch(graph, source):
    stack = [source]

    while len(stack) > 0:
        curr = stack.pop()
        print(curr)

        stack += graph[curr]


def depthFirstSearchRecur(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstSearchRecur(graph, neighbor)


GRAPH = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    "e": [],
    'f': []
}

print('First Way')
depthFirstSearch(GRAPH, 'a')
print('Second Way')
depthFirstSearchRecur(GRAPH, 'a')
