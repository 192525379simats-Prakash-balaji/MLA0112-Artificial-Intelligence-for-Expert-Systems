from collections import deque

capacity = (8, 5, 3)
start = (8, 0, 0)
goal = (4, 4, 0)

def transfer(state, i, j):
    s = list(state)

    amount = min(s[i], capacity[j] - s[j])

    s[i] -= amount
    s[j] += amount

    return tuple(s)

def bfs():
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for i in range(3):
            for j in range(3):
                if i != j:
                    new_state = transfer(state, i, j)

                    if new_state not in visited:
                        queue.append((new_state, path + [new_state]))

solution = bfs()

for state in solution:
    print(state)