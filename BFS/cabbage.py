from sys import stdin
from collections import deque
     

def bfs(x, y, count):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited[y][x] = count
    
    # Left , Right, Upper, Down 탐색
    queue = deque([(x,y)])
    
    while queue:
        x, y = queue.popleft()
        # 큐에서 pop        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]       
            # 상하좌우 이동
             
            if not (nx >= m or nx < 0 or ny >= n or ny < 0): # 리스트 범위 확인
                
                if (visited[ny][nx] != -1) or (cabbage[ny][nx] == 0): # 상하좌우에 양배추가 없거나 방문한적이 있다면
                    continue
                
                visited[ny][nx] = count # 조건 만족시 방문 처리
                queue.append((nx, ny)) # 큐에 삽입
            

tc = int(input())

for _ in range(tc):    # 테스트 케이스 반복
    m, n, k = map(int, stdin.readline().split())
    cabbage = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[-1 for _ in range(m)] for _ in range(n)] # 방문 처리
    
    cnt = 0 # bfs 반복 횟수
    
    for _ in range(k):    # 배추 위치 배열 만들기
        tmp1, tmp2 = map(int, stdin.readline().split())
        cabbage[tmp2][tmp1] = 1

    for i in range(n):
        for j in range(m):
            if(cabbage[i][j]==1) and (visited[i][j] == -1): 
                bfs(j,i,cnt)
                cnt += 1
    print(cnt)
