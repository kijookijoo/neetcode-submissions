class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq = Counter(t)
        seen = defaultdict(int)

        matching, needed = 0, len(freq)
        start = 0
        res = (-math.inf, math.inf)

        for i,c in enumerate(s):
            seen[c] += 1
            if c in freq and seen[c] == freq[c]:
                matching += 1
                # valid substring

            # while seen[s[start]] > freq[s[start]]:
            #     seen[s[start]] -= 1
            #     start += 1

            while matching == needed:
                if (i - start) < (res[1] - res[0]):
                    res = (start, i)

                seen[s[start]] -= 1
                if s[start] in freq and seen[s[start]] < freq[s[start]]:
                    matching -= 1
                start += 1            
            
        return "" if res == (-math.inf, math.inf) else s[res[0]: res[1] + 1]




        