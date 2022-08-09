#bfs
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        #we have to go for preorder only, the issue is we also have to do a simultaneous level order traversal.
        #for each level, we only assess the rights, if there are the rights, else we take in the lefts, in case there are no rights in that level.
        #summary:
        #level order traversal, but only pick the left nodes, iff right ones dont exist in that level.
        levels = []
        q = deque([root])
        while(q):
            for i in range(len(q)):
                node = q.popleft()
                if node!=None:
                    val = node.val
                if node!=None:
                    if node.left:
                        #then we dont go for left node
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            levels.append(val)
        return levels
            
            