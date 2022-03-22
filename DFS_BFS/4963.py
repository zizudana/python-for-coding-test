def dfs(x, y):
    global w, h, graph
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or ny <= -1 or nx >= w or ny >= h:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = -1
            dfs(nx, ny)


while(1):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [[] for _ in range(h)]
    for i in range(h):
        graph[i].append(list(map(int, input().split())))
    count = 0
    for i in range(w):
        for j in range(h):
            if graph[i][j] > 0:
                dfs(i, j)
                count += 1
    print(count)



