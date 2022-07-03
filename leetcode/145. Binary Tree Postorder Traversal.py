class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #left--right--root
        if not root:
            return []
        res = []
        def postorder(root):
            #left,right,root
            if not root:
                return 
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res