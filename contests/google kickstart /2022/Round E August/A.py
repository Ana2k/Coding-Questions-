def solve(): 
        #number of moves --> vali
        # x,y = map(int,input().split())        
        # maxi = 0
        # mat = [list(map(int,input().split())) for i in range(n)]
        n = int(input())
        # n,x = map(int,input().split())
        # s = input()
        # n,x,y = map(int,input().split())
        #dp O_O
        #represents the tiles.--> the valid moves possible in that tile
        #by the bot.
        dp = [0]*(n+1)

        dp[0] = 0
        for i in range(1,6):
            if i<=n:
                dp[i] = 1
        #it depends on how many peices of 5 can the number be divided into
        numFive = 0
        copy = n
        numFive = n//5
        print(numFive)
        #how many in 5--> 1
        return numFive+dp[n%5]
        
        # return dp[n]
        


        


            #GOOGLE KICKSTART B MAY 2022
        
t = int(input())
# t = 1
for _ in range(t):
    res = solve()
    print("Case #%d: %s" % ((_+1),res))