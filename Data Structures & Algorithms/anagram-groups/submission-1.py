class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = defaultdict(list)

        for i in range(len(strs)):
            sortedStr = "".join(sorted(strs[i]))
            groups[sortedStr].append(strs[i])

        res = [val for val in groups.values()]
        return res


        