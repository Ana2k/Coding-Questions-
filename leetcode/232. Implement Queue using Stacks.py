class MyQueue:
    def __init__(self):
        self.stk_q = []

    def push(self, x: int) -> None:
        self.stk_q.append(x)  
        # print(self.stk_q," PUSH")

    def pop(self) -> int:
        #popleft
        el = self.stk_q[0]
        stk_copy = self.stk_q[1::]
        self.stk_q = stk_copy
        # print(self.stk_q," POP",stk_copy,"EL",el)
        return el
        

    def peek(self) -> int:
        # print(self.stk_q,self.stk_q[0]," peek")
        return self.stk_q[0]
        

    def empty(self) -> bool:
        l = len(self.stk_q)
        # print(self.stk_q," empty",l)
        return l==0