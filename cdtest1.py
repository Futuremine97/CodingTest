from collections import deque, Counter
from functools import reduce

n = int(input())

a= [list(map(int,input())) for _ in range(n)]

group = [[0]*n for _ in range(n)]

dx =[-1,1,0,0]
dy =[0,0,-1,1]

def bfs(x,y,cnt):
      group[x][y] = cnt
      q = deque()
      q.append((x,y)) # 인접 노드 큐에 넣기
      while q: #큐가 빌때까지 
            x,y = q.popleft() #가장 먼저 들어온원소를 꺼냄
            for i in range(4):
                  nx,ny = x+dx[i], y+dy[i]
                  if 0 <= nx < n and 0 <= ny < n:
                        if group[nx][ny] == 0 and a[nx][ny] == 1:
                              group[nx][ny] == cnt
                              q.append((nx,ny))
            
cnt = 0

for i in range(n):
      for j in range(n):
            if group[i][j] == 0 and a[i][j] ==1:
                  cnt += 1
                  bfs(i,j,cnt)

result = reduce(lambda x,y : x+y, group)
result = [ i for i in result if i>0]
r = sorted(list(Counter(result).values()))

print(cnt)
for i in range(len(r)):
      print(i)

    