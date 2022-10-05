#Method 1
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # moves in a cycle prev(2)-->current(3)-->nxt(1) = current.next
        prev = None
        curr = head
        while(curr):
            #swap1
            nxt = curr.next
            curr.next = prev
            #swap2
            prev = curr
            curr = nxt
            # print(prev)
            # print(curr)
            # print(nxt)
            # print()
        return prev
#Method 2
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #another way to create an array reverse it tada lol
        res = []
        ptr = head
        while(ptr):
            res.append(ptr.val)
            ptr = ptr.next
        res = res[::-1]
        ans = ListNode(0)
        ptr = ans
        for x in res:
            ptr.next = ListNode(x)
            ptr = ptr.next
        return ans.next