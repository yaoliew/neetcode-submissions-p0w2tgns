class Solution:
    def isValid(self, s: str) -> bool:
        par_stack = []
        par_map = {")" : "(", "]" : "[", "}" : "{"}

        for ch in s:
            if par_stack and ch in par_map:
                if par_stack[-1] == par_map[ch]:
                    par_stack.pop()
                else:
                    return False
            elif ch in par_map:
                return False
            else:
                par_stack.append(ch)

        if len(par_stack) == 0:
            return True
        return False
