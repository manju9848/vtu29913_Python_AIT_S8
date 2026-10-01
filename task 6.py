# Frequency Assignment using Backtracking

def is_safe(tower, frequency, assignment, graph):
    for neighbor in graph[tower]:
        if assignment[neighbor] == frequency:
            return False
    return True


def frequency_assignment(tower, assignment, graph, frequencies):
    # All towers are assigned
    if tower == len(graph):
        return True

    # Try each available frequency
    for frequency in frequencies:
        if is_safe(tower, frequency, assignment, graph):
            assignment[tower] = frequency

            if frequency_assignment(tower + 1, assignment, graph, frequencies):
                return True

            # Backtrack
            assignment[tower] = 0

    return False


# Input
n = int(input("Enter number of towers: "))

print("Enter adjacency matrix:")
graph_matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    graph_matrix.append(row)

m = int(input("Enter number of frequencies: "))

# Convert adjacency matrix to graph
graph = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph_matrix[i][j] == 1:
            graph[i].append(j)

assignment = [0] * n
frequencies = list(range(1, m + 1))

# Solve
if frequency_assignment(0, assignment, graph, frequencies):
    print("\nValid Frequency Assignment:")
    for i in range(n):
        print("Tower", i + 1, "-> Frequency", assignment[i])
else:
    print("\nNo valid frequency assignment is possible.")
