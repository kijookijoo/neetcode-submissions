class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        
        for key, val in count.items():
            freq[val].append(key)
        
        res = []

        for l in range(len(freq) - 1, 0, -1):
            for n in freq[l]:
                if len(res) != k:
                    res.append(n)
                else:
                    return res
        
        return res
    




        
            


        