import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    global m, n, graph
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or ny <= -1 or nx >= m or ny >= n:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = -1
            dfs(nx, ny)


T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    count = 0
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for i in range(m):
        for j in range(n):
            if graph[i][j] > 0:
                dfs(i, j)
                count += 1
    print(count)
