#Lengthy but very very well explained.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #form list out of linkedlist for numbers
        def formList(l):
            ptr = l
            li = []
            while(ptr!=None):
                li.append(ptr.val)
                ptr = ptr.next
            return li
        #form a linkedlist out of list
        def formLL(n):
            carry = 0
            ptr = ans
            for i in range(n):
                curr = num1[i]+num2[i]+carry
                ptr.next = ListNode(curr%10)
                ptr = ptr.next
                carry = (curr//10)
            if carry>0:
                ptr.next = ListNode(carry)
                ptr = ptr.next
                
        #Step 1 : traverse the linkedlist and create two numbers(in reverse).
        #why reverse? bcs easier to add 0 that way for length mismatch
        num1 = formList(l1)
        num2 = formList(l2)
        
        #Step 2 : length correction,find number of zeroes and attatch to the end of smaller list.
        n = len(num1)
        m = len(num2)
        num_zeroes = abs(n-m)
        ans = ListNode()
        
        #Step3 : form the answer linkedlist, by calling formLL function :)
        if n>m:
            #add zeroes in num2
            num2 = num2+[0]*num_zeroes  
            formLL(n)
        else:
            num1 = num1+[0]*num_zeroes   
            formLL(m)
        return ans.next