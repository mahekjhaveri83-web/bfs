graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

queue = []
visited = []
start = 'A'

queue.append(start)
visited.append(start)

while queue:
    node = queue.pop(0)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.append(neighbor)
            queue.append(neighbor)
