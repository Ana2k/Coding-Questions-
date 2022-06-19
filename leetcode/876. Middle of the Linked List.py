class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast =slow = head
        while fast and fast.next:
            #almost always you will do a mistake
            #while(fast.next) then you will improve
            #while(fast and fast.next)
            fast = fast.next.next
            slow = slow.next
        return slow
            