class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                node = word[:i] + "*" + word[i + 1:]
                graph[node].append(word)
        
        count = 0
        q = deque([beginWord])
        visited = set()
        while q:
            count += 1
            for i in range(len(q)):
                curr = q.popleft()
                visited.add(curr)
                if curr == endWord:
                    return count
                for j in range(len(curr)):
                    regex = curr[:j] + "*" + curr[j + 1:]
                    q.extend([word for word in graph[regex] if word not in visited])
        
        return 0
                
            
    


                