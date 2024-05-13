from sys import stdin

n = int(stdin.readline())
nc = [3,5]

numcase = [[0 for _ in range(n)] for _ in range(2)]

for i in range(1,n+1):
    if(i%2 == 0):
        numcase[0][i//2] = 3
        
    if(i%4 == 0):
        numcase[1][i//4] = 5

print()
        
        
