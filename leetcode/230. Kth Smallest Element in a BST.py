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