class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = resPtr =ListNode(0)
        ptrA = list1
        ptrB = list2
        while(ptrA!=None and ptrB !=None):
            if ptrA.val<=ptrB.val:
                res.next = ListNode(ptrA.val)
                ptrA = ptrA.next
            else:
                res.next = ListNode(ptrB.val)
                ptrB = ptrB.next
            res = res.next
        while(ptrA):
            res.next = ListNode(ptrA.val)
            res = res.next
            ptrA = ptrA.next
        while(ptrB):
            res.next = ListNode(ptrB.val)
            res = res.next
            ptrB = ptrB.next
        return resPtr.next
