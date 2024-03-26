# leetcode 1번 Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        p1 = 0
        p2 = len(nums)-1
        ans = []
        sorted_nums = sorted(nums)
        while (p1<=p2):
            if (sorted_nums[p1] + sorted_nums[p2] == target):
                if (sorted_nums[p1] == sorted_nums[p2]):
                    ans = list(filter(lambda x: nums[x] == sorted_nums[p1], range(len(nums))))
                else:
                    ans = [nums.index(sorted_nums[p1]), nums.index(sorted_nums[p2])]
                break
            elif (sorted_nums[p1] + sorted_nums[p2] > target):
                p2 -= 1
            else:
                p1 += 1
        return ans