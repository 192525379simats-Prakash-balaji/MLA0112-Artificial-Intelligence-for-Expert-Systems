graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

def is_safe(node, color, assignment):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(assignment={}):
    if len(assignment) == len(graph):
        return assignment

    node = [n for n in graph if n not in assignment][0]

    for color in colors:
        if is_safe(node, color, assignment):
            assignment[node] = color

            result = map_coloring(assignment)
            if result:
                return result

            del assignment[node]

    return None

solution = map_coloring()

for region, color in solution.items():
    print(region, "->", color)