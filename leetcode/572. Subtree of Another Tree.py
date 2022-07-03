
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        def  sameTree(r,sR):
            if not r and not sR:
                return True
            if r and sR and (r.val==sR.val):
                return sameTree(r.right,sR.right) and sameTree(r.left,sR.left)
            return False
        if sameTree(root,subRoot):
            return True
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)