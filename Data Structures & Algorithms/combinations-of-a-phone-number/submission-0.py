class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }
        res = []
        if len(digits) == 0:
            return []

        def helper(curr, i):
            if i == len(digits):
                res.append("".join(curr.copy()))
                return
            
            for l in letters[digits[i]]:
                curr.append(l)
                helper(curr, i + 1)
                curr.pop()
        
        helper([], 0)
        return res
            
        