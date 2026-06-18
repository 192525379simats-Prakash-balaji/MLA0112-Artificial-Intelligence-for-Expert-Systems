from collections import deque


def is_valid(m, c):

    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and c > m:
        return False

    
    mr = 3 - m
    cr = 3 - c

    if mr > 0 and cr > mr:
        return False

    return True

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        m, c, boat = state

        moves = [
            (1, 0), 
            (2, 0), 
            (0, 1), 
            (0, 2), 
            (1, 1)   
        ]

        for dm, dc in moves:

            if boat == 1:  
                new_state = (m - dm, c - dc, 0)
            else:          
                new_state = (m + dm, c + dc, 1)

            if is_valid(*new_state[:2]) and new_state not in visited:
                queue.append((new_state, path + [new_state]))

    return None

solution = bfs()

print("Solution Path:")
for state in solution:
    print(state)