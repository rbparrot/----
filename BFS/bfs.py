from collections import deque

def bfs(node):
    queue = deque([node]) # 큐 자료구조 생성
    visited[node] = True # 1번노드 방문 처리
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        for i in graph[v]: # 리스트안의 리스트를 탐색
            if not(visited[i]):
                queue.append(i)
                visited[i] = True 
                
graph = [
    [],
    [2, 3], # 1번 노드와 연결된 노드들
    [1, 8], # 2번 노드와 연결된 노드들
    [1, 4, 5], # 3번 노드와 연결된 노드들 ...
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

visited = [False] * 9

bfs(1)
    