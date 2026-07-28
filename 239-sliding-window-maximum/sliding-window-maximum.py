from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        ans = []

        for i in range(len(nums)):

            # Remove indices outside the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Record the maximum once the first window is formed
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans