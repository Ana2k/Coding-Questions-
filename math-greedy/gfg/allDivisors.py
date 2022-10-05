#sum of all divisors till a given number
class Solution:
    def sumOfDivisors(self, N):
        sumTotal = 0
        for i in range(1,N+1):
            sumTotal+=(N//i)*i
        return sumTotal
# /// O(N) python solution ////

# Logic: 

# Count of i = N//i

# > Eg. Count of 2 if N=6 

# ==> 6//2 =3

 

# Value of those counts = (Count of i) * i

# > Eg. Value of 2's in N=6 

# ==> (Count of 2's in 6)  2 = (6//2)  2 = 3*2 = 6
    # # 	def sumEach(n):
    # # 	    #code here 
    # #     	sumi = 0
    # #     	for i in range(1,int((n)**0.5)+1):
    # #     	    if n%i==0:
    # #     	        if n//i==i:
    # #     	            sumi+=i
    # #     	           # print(i,"*",i,"=",i*i)
    # #     	        else:
    # #     	            sumi+=(i+(n//i))
    # #     	           # print(n//i,"*",i,"=",(n//i)*i)
    # #     	return sumi
    # 	for num in range(1,N+1):
    # 	    sumeach = (sumEach(num))
    # 	   # print(sumeach)
    # 	    sumTotal+=sumeach
    # 	return sumTotal