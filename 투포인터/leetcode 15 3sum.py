# leetcode 15 3sum
def threeSum(self, nums):
    ans = []
    nums.sort()
    for i in range(0, len(nums)-2):
        p1, p2 = i+1, len(nums)-1
        if (i>0 and nums[i]==nums[i-1]):
            continue
        two_sum = -nums[i]
        while (p1 < p2):
            if (nums[p1] + nums[p2] < two_sum):
                p1 += 1
            elif (nums[p1] + nums[p2] > two_sum):
                p2 -= 1
            else:
                ans.append([nums[i], nums[p1], nums[p2]])
                while (p1<p2 and nums[p1]==nums[p1+1]):
                    p1 += 1
                while (p1<p2 and nums[p2]==nums[p2-1]):
                    p2 -= 1
                p1 += 1
                p2 -= 1
    return ans