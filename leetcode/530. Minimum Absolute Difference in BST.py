class Solution:
    #Method 1 : make an array, sort and find the sum
    #nlogn 
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #any traversal - i choose postorder
        res = set()
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.add(root.val)
        dfs(root)
        res = list(res)
        res.sort()
        #find the minimum difference in this
        diff = float("inf")
        for i in range(1,len(res)):
            diff = min(diff,res[i]-res[i-1])
        return diff
            



    #Method 2 : inorder take advantage that this is a BST
    #n complexity
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #inorder traversal - uses left-root-right idea.
        # https://leetcode.com/problems/minimum-absolute-difference-in-bst/discuss/99913/Short-Simple-Python-O(N)-Time-O(N)-Space
        prev = diff = float("inf")
        def inorder(root):
            nonlocal prev,diff
            if not root:
                return 
            inorder(root.left)
            diff = min(diff,abs(root.val-prev))
            prev = root.val
            inorder(root.right)
        inorder(root)
        return diff