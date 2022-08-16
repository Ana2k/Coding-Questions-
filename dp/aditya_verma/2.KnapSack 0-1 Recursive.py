#1.0
# https://www.youtube.com/watch?v=kvyShbFVaY8&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=3

#How We came about to a base case
#think of reducing the input values to its lowest possible value

#like wt(W)-->  ultimately loweest that can be??(W-wt lowest?)  = 0
#number of objects we pick what is the lowest it can be?? = 0
#now think of the knapsack as a bag. 
#what is inside the bag, if the sum weight is 0 and the picked up weight also 0??
#its 0
#so our base casee becomes -->> if(wt==0 or n==0): 
# so recursive knapsack becomes sth like this:
#wt = wt array, val = val array, n = size of array, (i still dont understand why we are moving from the end.)
#W = the final wt capacity of the knapsack

def knapsack(wt,val,n,W):
    #base conditions
    #what is the lowest n can be?--> size of picking array? = 0
    #what is the lowest W can be? --> capacity of knapsack? =0
    #then what will be inside the knapsack in that iteration? = 0
    if n==0 or W==0:
        return 0
    # recursively the choice diagram is either take or not_take the current weight acc to its value
    take = val[n-1]+knapsack(wt,val,n-1,W-wt[n-1])
    not_take = knapsack(wt,val,n-1,W)
    if wt[i]<=W:
        return max(take,not_take)
    else:
        #wt[i]>W
        return not_take

