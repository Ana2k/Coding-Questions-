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
        stk = [root]
        while(stk):
            node = stk.pop()
            if node:
                if node.left:
                    stk.append(node.left)
                if node.right:
                    stk.append(node.right)
                temp = node.left
                node.left = node.right
                node.right = temp
        return  root

        