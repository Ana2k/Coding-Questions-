
#IMPORTANT !!!

        #Method 2 >> merge sort on linked list - TODO()
        #https://leetcode.com/problems/sort-list/discuss/1796857/Python-or-3-Solutions-or-Easy-and-Clean-Explained

#MEthod 1 >> does not count :/
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #how do we sort a linkedlist?
        # https://leetcode.com/problems/sort-list/discuss/1796857/Python-or-3-Solutions-or-Easy-and-Clean-Explained
        # for more methods
        #try the merge sort method to this sounds interesting.
        #Method 1 >> Convert to an arrray and then convert back.
        arr = []
        ptr = head
        while(ptr!=None):
            arr.append(ptr.val)
            ptr = ptr.next
        arr.sort()
        res = ptr2 = ListNode(0)
        for x in arr:
            res.next = ListNode(x)
            res = res.next
        return ptr2.next