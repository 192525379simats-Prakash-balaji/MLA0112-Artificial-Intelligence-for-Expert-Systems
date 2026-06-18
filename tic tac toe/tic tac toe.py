graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

def astar(start, goal):
    open_list = [(start, 0)]
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: x[1] + h[x[0]])
        node, cost = open_list.pop(0)

        if node == goal:
            return cost

        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                open_list.append((neighbor, cost + weight))

    return None

print("Cost =", astar('A', 'G'))