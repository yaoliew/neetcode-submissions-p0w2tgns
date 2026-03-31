class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    # 4 13 5 / + evaluates to 6: 13/5 = 2 -> 2 + 4 = 6
        ops = ["+", "-", "*", "/"]
        num_stack = []

        for t in tokens:
            if t in ops:
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                num_stack.append(self.operate(num2, t, num1))
            else:
                num_stack.append(int(t))
        return num_stack[0]

    def operate(self, base: int, op: str, num: int) -> int:
        if op == "+":
            return base + num
        if op == "*":
            return base * num
        if op == "-":
            return base - num
        return int(base / num)