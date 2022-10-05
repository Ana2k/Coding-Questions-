#TO SOLVE...
from collections import defaultdict
t = int(input())
def solve(s):
    alpha ="abcdefghijklmnopqrstuvwxyz"
    di = defaultdict(lambda : "")
    for i,ch in enumerate(alpha):
        di[i+1]=ch
for _ in range(t):
    s = input()
    print(solve(s))