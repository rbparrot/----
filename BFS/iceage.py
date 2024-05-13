from collections import deque
from sys import stdin
sys.setrecursionlimit(10**4)

def move(x, y):
    dx = [-1, 1, 0 , 0]
    dy = [0, 0, -1, 1]
    tmp = []
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if not (nx < 0 or nx >= cols or ny < 0 or ny >= rows):
            tmp.append((nx, ny))
    return tmp

def bfs(y, x):
    # x,y 는 좌표 
    visited.add((y, x))
    queue = deque([(y, x)])

    while queue:
        water_cnt = 0
        tmp1, tmp2 = queue.popleft()  # (y, x) 좌표가 나옴
        _moved = move(tmp2, tmp1) # (x, y) 좌표가 나옴
        
        for co in _moved:
            q_col, q_row = co
            if(ice_map[q_row][q_col]>0) and not ((q_row, q_col) in visited):
                queue.append((q_row, q_col))
                visited.add((q_row, q_col))
                
        if(ice_map[tmp1][tmp2]>0):
            for water in _moved:
                wx, wy = water
                if(ice_map[wy][wx]==0):
                    water_cnt += 1
            water_map[tmp1][tmp2] = water_cnt
            

        
rows, cols = map(int, stdin.readline().split())
day = 0

ice_map = [[] for _ in range(cols)]
water_map = [[0 for _ in range(cols)] for _ in range(rows)]

for j in range(rows):
    ice_map[j] = list(map(int, stdin.readline().split()))

# 배열 생성

while(True):
    bfs_cnt = 0
    ice_cnt = 0
    visited = set()
    
    
    for i in range(rows):
       for j in range(cols):
           if(ice_map[i][j] > 0):
               ice_cnt += 1
               if not ((i, j) in visited):
                   tmp = bfs(i,j)
                   bfs_cnt += 1
    
    
    if(ice_cnt==0):
        print(0)
        break;
    
    if(bfs_cnt>=2):
        print(day)
        break;
    
    
    for i in range(rows):
        for j in range(cols):
            if(ice_map[i][j]==0):
                continue
            
            ice_map[i][j] -= water_map[i][j]
            if(ice_map[i][j]<0):
                ice_map[i][j] = 0
                
    day +=1
                