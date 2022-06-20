class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch==")" and stack and stack[-1]=="(":
                stack.pop()
            elif ch=="]" and  stack and stack[-1]=="[":
                stack.pop()
            elif ch=="}" and  stack and stack[-1]=="{":
                stack.pop()
            else:
                stack.append(ch)
            
        return False if len(stack) else True