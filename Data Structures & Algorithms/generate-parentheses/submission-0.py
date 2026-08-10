class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, opened, closed):
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return

            if opened < n:
                curr.append("(")
                backtrack(curr, opened + 1, closed)
                curr.pop()

            if closed < opened:
                curr.append(")")
                backtrack(curr, opened, closed + 1)
                curr.pop()

        backtrack([], 0, 0)
        return res