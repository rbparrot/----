from sys import stdin

def make():
    if (n==1):
        return
    
    for i in range(n-1):
        for j in range(10):
            if(j==0):
                countList[i+1][j+1] += countList[i][j]
            elif(j==9):
                countList[i+1][j-1] += countList[i][j]
            else:
                countList[i+1][j+1] += countList[i][j]
                countList[i+1][j-1] += countList[i][j]
            
                
n = int(stdin.readline())

countList = [[0 for _ in range(10)] for _ in range(n)] # 각 자리수별로 저장
for i in range(10):
    countList[0][i] = 1
# 초깃값 설정

make()

# 출력 부분
if (n==1):
    print(sum(countList[0])-1)
else:
    print((sum(countList[n-1]) - countList[n-1][0]) % 1000000000)
