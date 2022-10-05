#first think and write the recursive code to this
def rec(level,li):#level represents - each row we are traversing. 
    #base cases

    # if "*" in li[level]:
        #we skip this row
    #compute
    #we take each column for each n queen subproblem.
    # for i in range(8):
    #     li[]
    #return
        

def solve():
    # n = int(input())
    # li = []
    # for i in range(8):
    #     s = list(input())
    #     li.append(s)
    # print(li)
    n = int(input())
    ans = rec(0,n)
    print(ans)

t = 1
while(t):
    solve()
    t-=1