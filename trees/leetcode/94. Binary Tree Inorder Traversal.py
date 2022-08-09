class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #remembere our arrow diagram of injectionn 
        # inorder = injection
        #  /\
        # /  \
        #/   *\*
        #iterative
        #simplest way to solve tree is almost always recursion
        res = []
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)
        traverse(root)
        return res