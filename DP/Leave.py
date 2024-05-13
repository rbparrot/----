from sys import stdin

n = int(input())
leave = []
money = [0 for _ in range(n)]

for i in range(n):
    key, value = map(int, stdin.readline().split())
    leave.append((key, value))
    
# 입력값 딕셔너리로 변환

for i in reversed(range(n)):
    if(i==n-1):
        if(leave[i][0]==1):
            money[i] = leave[i][1]
        continue
    # 마지막 일때
    
    if(leave[i][0]+ i <= n):
        money[i] = leave[i][1]
    
    tmp = [0]
    if not(i+leave[i][0]>=n):
            for j in range(i+leave[i][0],n):
                tmp.append(money[j])
                
    money[i] += max(tmp)
        
            
print(max(money))
        
# 브루트 포스
        
