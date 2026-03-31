class MinStack:
    # the key observation is that for any given prefix, the only values that matter for finding the min
    # later are the pushed values that actually become mins. That means we only need to do one comparison
    # between the current min and the new value instead of checking through the whole array
    # for a place to insert the new value. 

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
