#to minutely optimise 
# we can use variable -- to keep pathSum
#then use a flag variable called target.
#which breaks and returns recursion as soon as target is found.

class Solution:
#intuitive
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        if not root:
            return False
        def dfs(r,path):
            if not r.left and not r.right:
                path+=[r.val]
                res.append(path)
                return
            if r.left:
                dfs(r.left,path+[r.val])
            if r.right:
                dfs(r.right,path+[r.val])
            return 
        dfs(root,[])
        # print(res)
        for arr in res:
            if sum(arr)==targetSum:
                return True
        return False