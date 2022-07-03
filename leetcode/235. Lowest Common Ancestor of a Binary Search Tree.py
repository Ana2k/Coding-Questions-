class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #move to left of the root if both are lesser than the root
        if root.val>max(q.val,p.val):
            return self.lowestCommonAncestor(root.left,p,q)
        #move to right of the root if both are greater than the root
        elif root.val<min(q.val,p.val):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            #the root lies between p and q 
            # as a proper lca
            return root    