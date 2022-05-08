routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

def visit(point, car_cnt, board):
  visited = [1] * car_cnt
  cnt = 0
  for car_idx in range(car_cnt):
    if visited[car_idx] == 1:
      if point in board[car_idx]:
        visited[car_idx] = 0
        cnt += 1
  print(visited)
  return cnt

def solution(routes):
  answer = 1e9
  car_cnt = len(routes)
  points = []
  for car in routes:
    for i in car:
      if i not in points:
        points.append(i)

  board = [[] for _ in range(car_cnt)]
  for car_idx in range(car_cnt):
    for point in points:
      if (routes[car_idx][0]<=point<=routes[car_idx][1]):
        board[car_idx].append(point)
  for point in points:
    answer = min(visit(point, car_cnt, board), answer)
  return answer

print(solution(routes))