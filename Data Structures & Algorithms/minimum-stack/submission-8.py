class MinStack:

    def __init__(self):
        self.main_stack = []
        self.second_stack = []
        

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.second_stack or val <= self.second_stack[-1]:
            self.second_stack.append(val)
        

    def pop(self) -> None:
        if self.second_stack and self.main_stack[-1] == self.second_stack[-1]:
            self.main_stack.pop()
            self.second_stack.pop()
        elif self.main_stack:
            self.main_stack.pop()
        

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack.pop()
        return 0
        

    def getMin(self) -> int:
        if self.second_stack:
            return self.second_stack[-1]
        else:
            return 0

        
