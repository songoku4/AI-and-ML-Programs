import math
maxsize = float('inf')
def fin(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]
def fMin(adj, i):
    min = maxsize
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]

    return min
def sMin(adj, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]

        elif(adj[i][j] <= second and
            adj[i][j] != first):
            second = adj[i][j]

    return second
def TS(adj, curr_bound, curr_weight,
            level, curr_path, visited):
    global final_res
    if level == N:
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + adj[curr_path[level - 1]]\
                                        [curr_path[0]]
            if curr_res < final_res:
                fin(curr_path)
                final_res = curr_res
        return
    for i in range(N):
        if (adj[curr_path[level-1]][i] != 0 and
                            visited[i] == False):
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]
            if level == 1:
                curr_bound -= ((fMin(adj, curr_path[level - 1]) +
                                fMin(adj, i)) / 2)
            else:
                curr_bound -= ((sMin(adj, curr_path[level - 1]) +
                                fMin(adj, i)) / 2)
            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True
                TS(adj, curr_bound, curr_weight,
                    level + 1, curr_path, visited)
            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp
            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True

def TP(adj):
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N
    for i in range(N):
        curr_bound += (fMin(adj, i) +
                    sMin(adj, i))
    curr_bound = math.ceil(curr_bound / 2)
    visited[0] = True
    curr_path[0] = 0
    TS(adj, curr_bound, 0, 1, curr_path, visited)
adj = [[0, 5, 15, 10],
    [30, 0, 5, 5],
    [10, 30, 0, 40],
    [15, 20, 30, 0]]
N = 4
final_path = [None] * (N + 1)
visited = [False] * N
final_res = maxsize
TP(adj)
print("Minimum cost:", final_res)
print("Path: ", end = ' ')
for i in range(N + 1):
    print(final_path[i], end = ' ')

