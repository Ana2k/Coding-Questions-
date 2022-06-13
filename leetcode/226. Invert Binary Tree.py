#Method 1 : recursive but complexity bad.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        #recursive swapping
        temp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp
        
        return root
#Method 2 : bfs
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        #recursive swapping
        q = [root]
        while(q):
            r = q.pop()
            if r:
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
                temp = r.left
                r.left = r.right
                r.right = temp
        return  root

        