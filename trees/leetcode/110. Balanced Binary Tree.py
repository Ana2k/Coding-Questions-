class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #think about when is the subtree not balanced?
        #when abs(left_ht-right_ht)>1 or we can say 
        # MAIN CONDITION FOR BALANCED TREE: to stay balanced we need abs(left_ht-right_ht)<=1
        
        #function check returns max-height of the tree or -1
        #why are we returning height of the tree?
        #look closely at left_ht and right_ht, they are the left height and the right height associated with the left subtree and right subtree.(unless they already became -1)
        def check(root):
            if not root:
                return 0
            lh,rh = check(root.left),check(root.right)
            if lh==-1 or rh==-1 or abs(lh-rh)>1:
                return -1
            else:
                return max(lh,rh)+1
        
        return check(root)!=-1