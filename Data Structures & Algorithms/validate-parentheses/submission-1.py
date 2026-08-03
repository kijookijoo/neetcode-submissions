class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for c in s:
            if c in parens:
                stack.append(parens[c])
            else:
                if not stack or stack[-1] != c:
                    return False
                stack.pop()
        return len(stack) == 0
                
            