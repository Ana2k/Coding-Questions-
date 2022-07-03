class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
# https://leetcode.com/problems/sum-of-left-leaves/discuss/2228108/Python3-or-Simple-Recursion        
        if not root:
            return 0
        def leftLeaves(root):
            if root==None:
                return 0
            #the root's left is a leftLeave :)
            #now check the right part of this root 
            if root.left and root.left.left==None and root.left.right==None:
                return root.left.val+leftLeaves(root.right)
            return leftLeaves(root.left)+leftLeaves(root.right)
        return leftLeaves(root)