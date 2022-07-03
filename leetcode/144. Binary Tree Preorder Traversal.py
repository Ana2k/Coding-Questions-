class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #root,left,right
        if not root:
            return []
        res = []
        def preorder(root):
            if not root:
                return 
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res