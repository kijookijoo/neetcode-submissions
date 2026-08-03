class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
                continue
            ops1, ops2 = stack.pop(), stack.pop()
            if t == "+":
                res = ops1 + ops2
            elif t== "-":
                res = ops2 - ops1
            elif t == "/":
                res = int(ops2 / ops1)
            elif t == "*":
                res = ops1 * ops2
            stack.append(res)
        
        return stack[-1]