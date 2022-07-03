class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(r,path):
            if not r.left and not r.right:
                path += str(r.val)
                res.append(path)
                return
            if r.left:
                dfs(r.left, path+str(r.val)+"->")
            if r.right:
                dfs(r.right, path+str(r.val)+"->")
            return
        dfs(root,"")
        return res