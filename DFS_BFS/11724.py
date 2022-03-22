import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


count = 0
for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)