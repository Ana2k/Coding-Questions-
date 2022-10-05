t = int(input())
def solve(a,b,c):
    val1 = abs(a-1)
    val2 = abs(b-c)+abs(c-1)
    if val1==val2:
        return 3
    elif val1>val2:
        return 2
    else:
        return

    return


for _ in range(t):
    a,b,c = map(int,input().split())
    print(solve(a,b,c))