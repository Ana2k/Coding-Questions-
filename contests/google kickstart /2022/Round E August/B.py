def solve(): 
        #number of moves --> vali
        # x,y = map(int,input().split())        
        # maxi = 0
        # mat = [list(map(int,input().split())) for i in range(n)]
        n = int(input())
        # n,x = map(int,input().split())
        # s = input()
        # n,x,y = map(int,input().split())
        ratings = list(map(int,input().split()))
        res = [0]*(n)
        ratings_idx = [(ratings[i],i) for i in range(n)]
        ratings_idx = sorted(ratings_idx,key = lambda x : x[0])
        print(ratings_idx)
        # di = {}

        
        for i in range(n):
            curr = ratings[i]
            low = 0
            high = n-1
            while(low<high):
                # mid = (low+high)//2
                # if ratings_idx[mid][0]<=2*curr:
                #     if ratings_idx[mid][1]!=i:
                #         res[i] = max(ratings_idx[i][0],res[i])
                #     #move up.
                #     low = mid+1
                # high = mid-1
            if res[i]==0:
                res[i]=-1

        return res
        



        



t = int(input())
# t = 1
for _ in range(t):
    #this is a list
    res = solve()
    print("Case #%d: " %(_+1))
    for x in res:
        print(x,end=" ")
    print()