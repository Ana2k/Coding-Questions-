class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/726732/Python-10-lines-BFS-explained-with-figure
        #basically level order traversal only. with multiple params.
        if not root: return 0
        q = [(root,0)]
        maxi = 0
        while q: 
            maxi = max(maxi,q[-1][1]-q[0][1]+1)
            temp = []
            for node,idx in q:
                if node.left: temp.append([node.left,2*idx])
                if node.right:temp.append([node.right,2*idx+1])
            q = temp
        return maxi