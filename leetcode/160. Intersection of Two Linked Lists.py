class Solution:    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #brute force find the pathway till the intersection of
        #both the nodes iterate till there bobth the heads
        def size(ptr):
            size = 0
            while(ptr):
                size+=1
                ptr = ptr.next
            return size
        sizeA = size(headA)
        sizeB = size(headB)
        diff = abs(sizeA-sizeB)
        
        #idea get both the pointers to the the starter point of intersection
        #and then start the two pointer iteration
        ptrA = headA
        ptrB = headB
        if sizeA>sizeB:
            i=0
            while(i<diff):
                ptrA = ptrA.next
                i+=1
        else:
            i=0
            while(i<diff):
                ptrB = ptrB.next
                i+=1
        while(ptrA!=ptrB):
            ptrA = ptrA.next
            ptrB = ptrB.next
        return ptrA