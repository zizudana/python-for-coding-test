n = int(input())
m = int(input())
graph = [[0] * (n+1) for i in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(v):
    visited[v] = True
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


dfs(1)
count = 0
for i in visited:
    if i:
        count += 1
print(count-1)
