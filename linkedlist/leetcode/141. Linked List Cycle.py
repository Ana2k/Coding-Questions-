#Method 1
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    #Step 1 : traverse a Linked list and check if any of the ptr are repeating through a set
    #Space : o(N)

        st = set()
        ptr = head
        while(ptr):
            if ptr in set:
                return True
            st.add(ptr)
            ptr = ptr.next
        return False
#Method 2
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    #Step 2 : Rabbit and Hare method.
    #  Eventually the pointers will become the same, we check for such a case.
    # Either the traversal is complete or the pointers become same :)
    #Space : o(1)
        fast = slow = head
        #middle of linkedlist logic
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                return True
        return False
