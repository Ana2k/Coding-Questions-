class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #not a binary search so, we have to check. but how?
        #https://afteracademy.com/blog/lowest-common-ancestor-of-a-binary-tree
        #do dfs, when you can say left and right for a particular node returns , node1 and node2 
        #or in case lca is either node, then subtrees have the other node. 
        #then we say ok this is the lca.
        #still does not make a lot of sense to me.
        # but lets give it a good shot.
        if not root:
            return None
        #base case
        if root==None or root==p or root==q:
            return root
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)
        #if nothing was found in the left side
        #we say ok, check the right side
        if not l:
            return r
        #if nothing was found on the right side 
        #we say ok check the left side
        if not r:
            return l
        #means both returned. 
        #that means the current root is a possible lca
        else:
            return root