from sys import stdin
from collections import deque

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([])
    
    for key in (list(visited.keys())[:]): # BFS 시작
        col, row = key
        queue.append((row, col))
    
    
    # Left , Right, Upper, Down 탐색
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i] 
            
            if not (nx >= m or nx < 0 or ny >= n or ny < 0): # 리스트 범위 확인
                if(tomato[ny][nx] == -1) or (visited.get((ny,nx)) != None): # 상하좌우에 토마토가 없다면, 방문한적이 있다면
                    continue
                
                # if(visited.get((ny,nx)) == None): # 방문한적이 없다면
                
                visited[(ny,nx)] = visited.get((y, x)) + 1 
                queue.append((nx,ny))
                
                
m, n = map(int, stdin.readline().split())
tomato = [0 for _ in range(n)]
visited = {}

for i in range(n): # 방문 딕셔너리 만들기
    tmp = list(map(int, stdin.readline().split()))
    tomato[i] = tmp[:]
    for j in range(len(tmp)):
        if(tmp[j]==1):
            visited[(i,j)]=0 # i = 행, j = 열



bfs()


# 결과값 출력
try:
    for i in range(n):
        for j in range(m):
            if(visited.get((i,j))==None) and (tomato[i][j]==0):
                raise NotImplementedError
except:
    print(-1)
else:
    print(max(visited.values()))    
    
