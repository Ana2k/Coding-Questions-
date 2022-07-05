#METHOD 1 : RECURSION non optimised
# METOD 2: https://medium.com/nerd-for-tech/convert-sorted-array-to-binary-search-tree-61eccf6df812
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #how this is tough?
        #but how do we do this?
        #height balnacedddD????? TF????
        
        # https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/1363643/Python3-Two-Solutions-Explained-with-Diagrams
        #points to note 1) the mid element is always the recursive node
        #now look at the other recursive nodes, on left and the right 
        #they are mids too. say i have an array [1,2,3,4,5,6,7]
        #then the mid --> 4 is the root.
        #again, look at the mid of the sub-arrays, meaning,
        #mid of [1,2,3] and [5,6,7]--> 2 becomes the left node and 6 becomes the right node.
        #so the new tree becomes:
        # same as the diagram in the above link.
        #code:
        if not nums:
            return
        mid = len(nums)//2
        root_node = TreeNode(nums[mid])
        root_node.left = self.sortedArrayToBST(nums[:mid])
        #leave the mid its already the root node
        root_node.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root_node
        
        