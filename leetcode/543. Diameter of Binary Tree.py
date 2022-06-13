#Method 1 : Recursive
class Solution:
    def __init__(self):
        self.max = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = leftnode+rightnode+1
        # https://favtutor.com/blogs/binary-tree-diameter
        #Method 1 recursive method

        def traverse(root):
            if root is None:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            if left+right>self.max:
                self.max = left+right
            return max(left,right)+1
        traverse(root)
        return self.max



        
# #Method 2 : iterative - 1
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
#         stk = deque([root])
#         depth = {}
#         dia = 0
#         # https://leetcode.com/problems/diameter-of-binary-tree/discuss/234397/C%2B%2B-recursive-and-iterative
#         # https://leetcode.com/problems/diameter-of-binary-tree/discuss/1351854/Python-Iterative-solution-40-ms-faster-than-90.06-15.2-MB-less-than-99.95
#         #Method 2 = iterative
#         while(stk):
#             node = stk[-1]
#             if node:
#                 if node.left and depth.get(node.left)==None:
#                     stk.append(node.left)
#                 elif node.right and depth.get(node.right)==None:
#                     stk.append(node.right)
#                 else:
#                     stk.pop()
#                     l,r = depth.get(node.left,0),depth.get(node.right,0)
#                     depth[node] = max(l,r)+1
#                     dia = max(dia,l+r)
#         return dia
# #Method 2.1 - iterative - 2
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
#         stk = [(root,False)]
#         depth = {}
#         dia = 0
#         # https://leetcode.com/problems/diameter-of-binary-tree/discuss/234397/C%2B%2B-recursive-and-iterative
#         # https://leetcode.com/problems/diameter-of-binary-tree/discuss/1351854/Python-Iterative-solution-40-ms-faster-than-90.06-15.2-MB-less-than-99.95
#         #Method 2 = iterative
#         #post order in both recursive as well as iterative.
#         while(stk):
#             node,visited = stk.pop()            
#             if node:
#                 if visited:
#                     lh = depth.get(node.left,0)
#                     rh = depth.get(node.right,0)
#                     depth[node] = max(lh,rh)+1
#                     dia = max(dia,lh+rh)
#                 else:
#                     stk.append((node,True))
#                     stk.append((node.left,False))
#                     stk.append((node.right,False))
#         return dia
