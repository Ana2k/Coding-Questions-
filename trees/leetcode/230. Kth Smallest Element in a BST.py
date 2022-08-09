#Method 1 space O(1)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #inorder?
        res = 0
        def inorder(root):
            nonlocal res,k
            if k>=1:
                if not root:
                    return
                inorder(root.left)
                if k>=1:
                    res = (root.val)
                    k-=1
                inorder(root.right)
                # print(res," ",k)
        inorder(root)
        return res

#Method 2 space O(2)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

#method 2 with heap--> easier to implement but spaceO(n)
        heap = []
        heapq.heapify(heap)
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            heapq.heappush(heap,node.val)
            inorder(node.right)
        inorder(root)
        while(k-1):
            heapq.heappop(heap)
            k-=1
        return heapq.heappop(heap)
        