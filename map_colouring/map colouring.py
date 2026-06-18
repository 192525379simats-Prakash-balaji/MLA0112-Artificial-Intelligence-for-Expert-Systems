import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

def ucs(start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            return cost

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            heapq.heappush(pq, (cost + weight, neighbor))

    return None

print("Cost =", ucs('A', 'G'))