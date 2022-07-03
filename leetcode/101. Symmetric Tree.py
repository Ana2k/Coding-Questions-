class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left,root.right)
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            return self.isSameTree(p.right,q.left) and self.isSameTree(p.left,q.right)
        return False