#%%
# 1.Two Sum
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
from matplotlib.cbook import index_of
from pygments import highlight


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(i+1 ,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))
print(s.twoSum(nums = [3,2,4], target = 6))
print(s.twoSum(nums = [3,3], target = 6))


#%%
# 9. Palindrome Number
'''
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
cs'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        inp = [i for i in str(x)]
        n = len(inp)

        res = [0]*len(inp)
        for ind in range(n):
            res[n-1-ind] = inp[ind]

        print(str(x))
        print(''.join(res))
        return True if ''.join(res) == str(x) else False

s = Solution()
print(s.isPalindrome(x = 121))
print(s.isPalindrome(x = -121))
print(s.isPalindrome(x = 10))


# %%
# 11. Container With Most Water
'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
'''

class Solution(object):
    # naive solution. runtime O(n^2)
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        res = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
               water = min(height[i], height[j]) * (j-i)
               res = water if water > res else res
        return res

    # improved solution. O(n)
    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        j = len(height) - 1
        res = max(res, min(height[i], height[j]) * (j - i))
        while(i < j):
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i = i + 1
            else:
                res = max(res, height[j] * (j - i))
                j = j - 1

        return res

s = Solution()
height = [1,8,6,2,5,4,8,3,7]

# height = [1,1]

print(s.maxArea2(height))

# %%
