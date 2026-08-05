class MonotonicQueue:
    def __init__(self):
        self.q = deque()
        self.max_q = deque()
    
    def pop(self, val) -> None:
        self.q.popleft()
        if self.max_q and self.max_q[0] == val:
            self.max_q.popleft()

    def top(self) -> int:
        return self.q[0]

    def getMax(self):
        return self.max_q[0]

    def push(self, val):
        self.q.append(val)
        while self.max_q and self.max_q[-1] < val:
            self.max_q.pop()
        self.max_q.append(val)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = MonotonicQueue()
        for i in range(k):
            q.push(nums[i])

        res = [q.getMax()]

        for i in range(k, len(nums)):
            q.pop(nums[i - k])
            q.push(nums[i])
            res.append(q.getMax())

        return res














        