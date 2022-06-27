#tree - dfs - can use visited with traverse if you want.

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left+right+1