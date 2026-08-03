class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        q = collections.deque()

        for par in s:
            if par in parens.values():
                if q:
                    comp = q.pop()
                else:
                    return False
                if parens[comp] != par:
                    return False
            else:
                q.append(par)
        
        return True if not q else False
            
            


        