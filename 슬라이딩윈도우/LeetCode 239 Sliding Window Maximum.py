# LeetCode 239 Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/description/

import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        ans = []
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i],i))
        ans.append(-heap[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i],i))
            while (heap[0][1] <= i-k):
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans
