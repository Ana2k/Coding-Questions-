class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/1219538/Python-Simple-bfs-explained
        if not root:
            return []
        levels = []
        q = deque([root])
        while(q):
            #store all the elements in deque and pop from left
            #for each level
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            levels.append(level)
        return levels