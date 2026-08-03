class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for char in s:
            count[char] += 1
        
        for char in t:
            if count[char] - 1 < 0:
                return False
            elif count[char] - 1 == 0:
                del count[char]
            else:
                count[char] -= 1
        

        return True if not (count) else False

            
        