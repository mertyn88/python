vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4), (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]
#       0
#      | \
#      1  2
#      |  | \
#      3  4  5
#         |
#         6


def bfs(vertexList, edgeList, start):
    visitedList = []
    queue = [start]
    adjacencyList = [[] for _ in vertexList]

    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # bfs
    while queue:
        current = queue.pop(0)
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.append(neighbor)
        visitedList.append(current)
    return visitedList

print(bfs(vertexList, edgeList, 0))