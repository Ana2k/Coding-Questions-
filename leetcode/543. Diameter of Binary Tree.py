#Method : Recursive
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = leftnode+rightnode+1
        # https://favtutor.com/blogs/binary-tree-diameter
        #Method 1 recursive method
        dia = 0
        #recursive
        def move(root):
            nonlocal dia
            if root is None:
                return 0
            left = move(root.left) 
            right = move(root.right)
            dia = max(dia,left+right)
            return max(left,right)+1

        move(root)
        return dia

        
#Method 2 : iterative 
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stk = [root]
        depth = defaultdict(lambda : 0)
        dia = 0
        while(stk):
            node = stk[-1]
            if node:
                if node.left and depth[node.left]==0:
                    stk.append(node.left)
                elif node.right and depth[node.right]==0:
                    stk.append(node.right)
                else:
                    stk.pop()
                    l,r = depth[node.left],depth[node.right]
                    depth[node] = max(l,r)+1
                    dia = max(dia,l+r)
        return dia
