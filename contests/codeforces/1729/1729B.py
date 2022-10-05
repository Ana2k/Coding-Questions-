from collections import defaultdict
t = int(input())
def solve(code,n):
    alpha ="abcdefghijklmnopqrstuvwxyz"
    di = defaultdict(lambda : "")
    for i,ch in enumerate(alpha):
        di[i+1]=ch
    # "di)
    res = []
    i = 0
    while(i<n):
        num = code[i]
        if num=="0":
            #meaning last two entries were false.
            #or its a ten,twenty in which case it will be followed by a zero
            if i<n-1 and code[i+1]=="0":
                #case for a 10.
                #this means its a 10.
                res.pop()
                res.append(di[int(code[i-1])*10])
                i+=1
                # "res)
            else:
                #case for a double digit.
                #the last two entries were false
                # "res,"BEFORE")
                res.pop()
                res.pop()
                units = int(code[i-1])
                tens = int(code[i-2])*10
                key = units+tens
                # "key)
                res.append(di[key])                
                # "res,"AFTER")
        else:
            res.append(di[int(num)])
        i+=1
    # "res)
    return ''.join(res)
for _ in range(t):
    n = int(input())
    code = input()
    print(solve(code,n))