class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #inorder traversal. and make sum or an array?
        #BST means inorder --- wakarimasu ka? 
        #brute force first
        sumi = 0
        def inorder(root):
            nonlocal sumi
            if not root:
                return
            inorder(root.left)
            if low<=root.val<=high:
                sumi+=root.val
            inorder(root.right)
            
        inorder(root)
        return sumi