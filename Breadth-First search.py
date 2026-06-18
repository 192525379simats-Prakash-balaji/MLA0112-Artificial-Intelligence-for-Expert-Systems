from collections import deque

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2, 5],
    5: [2, 4]
}

def bfs(start):
    visited = set([start])
    q = deque([start])
    order = []

    while q:
        node = q.popleft()
        order.append(node)

        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                q.append(neigh)

    return order



print("BFS:", bfs(1))


