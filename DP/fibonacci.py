"""from sys import stdin

def fibonacci(n):
    for i in range(n+1):
        if(i==0):
            fib[i] = [1, 0]
        elif(i==1):
            fib[i] = [0, 1]
        elif(i==2):    
            fib[i] = [1, 1]
        else:
            fib[i] = [fib.get(i-1)[0] + fib.get(i-2)[0],fib.get(i-1)[1]+ fib.get(i-2)[1]]
  

    
tmp = int(stdin.readline())
fib = {}

for _ in range(tmp):
    n = int(stdin.readline())
    fibonacci(n)
    print(fib[n][0], fib[n][1])

"""
from sys import stdin

class fib:
    def __init__(self, zero, one):
        self.cnt_zero = zero
        self.cnt_one = one

def fibonacci(n):
    for i in range(n+1):
        if(i==0):
            fibo[i] = fib(1, 0)
        elif(i==1):
            fibo[i] = fib(0, 1)
        elif(i==2):    
            fibo[i] = fib(1, 1)
        else:
            fibo[i] = fib(fibo[i-1].cnt_zero + fibo[i-2].cnt_zero, fibo[i-1].cnt_one + fibo[i-2].cnt_one)
  

    
tmp = int(stdin.readline())


for _ in range(tmp):
    n = int(stdin.readline())
    fibo = [-1 for _ in range(n+1)]
    fibonacci(n)
    print(fibo[n].cnt_zero, fibo[n].cnt_one)