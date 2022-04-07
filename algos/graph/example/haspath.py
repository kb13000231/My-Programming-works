"""
Write a function, hasPath, that takes in an object
representing the adjacency list of a directed acyclic
graph and two nodes (src, dst). The function should
return a boolean indicating whether or not there exists
a directed path between the source and destination nodes.

"""


def hasPath(graph, src, dst):
    stack = [src]

    while len(stack) > 0:
        curr = stack.pop()
        if curr == dst:
            return True
        stack += graph[curr]
    return False


graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
# 1
print(1)
print(hasPath(graph, 'f', 'j'))  # false

# 2
print(2)
print(hasPath(graph, 'i', 'h'))  # true
