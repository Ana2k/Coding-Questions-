#Method 1
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
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
        fast = slow = head
        #middle of linkedlist logic
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                return True
        return False
