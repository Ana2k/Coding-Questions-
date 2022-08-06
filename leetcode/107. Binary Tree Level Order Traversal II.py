#level order - tree - bfs
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        levels = []
        while(q):
            level = []
            for i in range(len(q)):
                node = q.popleft()
                #root-->left-->right
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            levels.append(level)
        return levels[::-1]