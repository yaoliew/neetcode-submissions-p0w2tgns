class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            for ch in string:
                ans += str(ord(ch)) + "x"
            ans += "y"
        return ans
    def decode(self, s: str) -> List[str]:
        res = [""] * s.count("y")
        index = 0
        temp = ""
        for ch in s:
            if ch == "y":
                index += 1
            elif ch == "x":
                res[index] += chr(int(temp))
                temp = ""
            else:
                temp += str(ch)
        return res
