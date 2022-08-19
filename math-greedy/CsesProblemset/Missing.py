# https://cses.fi/problemset/task/1083
from collections import Counter 
def solver():
    n = int(input())
    li = list(map(int,input().split()))
    #brute force = sorts
    di = Counter(li)
    for x in range(1,n+1):
        if x not in di:
            return x


t = 1
while(t):
    ans = solver()
    print(ans)
    t-=1
