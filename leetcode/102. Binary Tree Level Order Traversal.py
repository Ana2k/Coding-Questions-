#binary - tree - bfs - level order
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/1219538/Python-Simple-bfs-explained
        #bfs over tree
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
                level.append(node.val) #root
                if node.left: q.append(node.left) #left
                if node.right: q.append(node.right) #right
            levels.append(level)
        return levels
    
    #DFS
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     levels = []
    #     if not root:
    #         return []
    #     def dfs(node,depth):
    #         if len(levels)==depth:
    #             levels.append([])
    #         levels[depth].append(node.val)               
            
    #         if node.left:
    #             dfs(node.left,depth+1)
    #         if node.right:
    #             dfs(node.right,depth+1)
            
    #     dfs(root,0)
    #     return levels