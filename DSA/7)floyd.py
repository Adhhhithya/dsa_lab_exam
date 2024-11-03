# Number of vertices
nV = 4
INF = 999

# Floyd-Warshall algorithm
def floyd_warshall(G):
    # Copy the input graph into the distance matrix
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Updating the distance matrix for each vertex as an intermediate point
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    print_solution(distance)

# Print the solution matrix
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print("")

# Input graph with weights (INF represents no direct path)
G = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

# Execute the Floyd-Warshall algorithm
floyd_warshall(G)
