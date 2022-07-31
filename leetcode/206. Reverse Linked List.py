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