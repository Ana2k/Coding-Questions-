class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        count_left = self.maxDepth(root.left)+1
        count_right = self.maxDepth(root.right)+1
        return max(count_left,count_right)