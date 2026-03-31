class Solution:
    def isValid(self, s: str) -> bool:
        par_stack = []
        for ch in s:
            if ch in ["(", "[", "{"]:
                par_stack.append(ch)
            if ch == ")":
                if len(par_stack) > 0 and par_stack[-1] == "(":
                    par_stack.pop()
                else:
                    return False
            if ch == "]":
                if len(par_stack) > 0 and par_stack[-1] == "[":
                    par_stack.pop()
                else:
                    return False
            if ch == "}":
                if len(par_stack) > 0 and par_stack[-1] == "{":
                    par_stack.pop()
                else:
                    return False
        
        if len(par_stack) == 0:
            return True
        return False