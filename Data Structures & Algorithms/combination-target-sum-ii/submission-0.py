class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(curr, total, i):
            if total > target:
                return
            if total == target:
                res.append(curr.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                curr.append(candidates[j])
                backtrack(curr, total + candidates[j], j + 1)
                curr.pop()
        
        backtrack([], 0, 0)
        return res
        