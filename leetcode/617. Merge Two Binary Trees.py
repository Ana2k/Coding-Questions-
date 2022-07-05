#SHORT
class Solution:
    def mergeTrees(self, root1, root2):
        if not root1: return root2
        if not root2: return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

#DETAIlED
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #so there are two trees, and if the nodes overlap, then add those nodes.val
        #if they dont then make them branches in the tree
        # how do we recurse through the tree to do so?think.
        #my thought was right but not the implementation.
        #can find how to think this question on : https://www.youtube.com/watch?v=lw5swOzpFtE&ab_channel=AlgorithmsMadeEasy
        #will mostly follow this but,https://leetcode.com/problems/merge-two-binary-trees/discuss/2111599/Python-Depth-first-Search-Recursion-Solution-(97-Time-78.40-Space)
        #as i am planning on creating a new tree.
        
        def dfs(root,root1,root2):
            #main conditions are what to send when each root is None in pnc
            if root1==None and root2==None:
                return None
            elif root1==None and root2!=None:
                return root2
            elif root2==None and root1!=None:
                return root1
            else:
                root = TreeNode(root1.val+root2.val)
                root.left = dfs(root,root1.left,root2.left)
                root.right = dfs(root,root1.right,root2.right)
                return root
            
        res = dfs(None,root1,root2)
        return res