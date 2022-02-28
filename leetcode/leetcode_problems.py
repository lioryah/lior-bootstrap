#%%
# 1.Two Sum
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
from typing import List
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
# 53. Maximum Subarray
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
'''
import itertools

class Solution:
    
    def maxSubArray(self, nums) -> int:
        accumulated_nums = [x for x in itertools.accumulate(nums)]
        
        l = len(accumulated_nums)
        if l == 1:
            return nums[0]
        start = 0
        end = 1
        for i in range(1,l):
            if accumulated_nums[i] > accumulated_nums[i-1]:
                end = i
            else:
                start = i
        
        return accumulated_nums[end] - accumulated_nums[start]



    def maxSubArray2(self, nums) -> int:
        final_list = [max(nums)]
        max_num = nums[0]
        if max(nums) > 0:
            for element in nums[1:len(nums)]:				
                if max_num < 0:
                    max_num = 0			
                    max_num += element
                final_list.append(max_num)

        return sorted(final_list)[-1]


s = Solution()
inp = [-2,1,-3,4,-1,2,1,-5,4]
print("not mine " + str(s.maxSubArray2(inp)))
inp = [1]
s.maxSubArray(inp)
inp = [5,4,-1,7,8]
s.maxSubArray(inp)


# %%
# 139. Word Break
'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''  
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:        
        while s != '':
            for i in range(len(s)+1):
                print(s[:i])
                if s[:i] in wordDict:
                    if Solution.wordBreak(self, s = s[i:], wordDict = wordDict):
                        print(s[i:])
                        return True
                    else:
                        continue
            return False
        else:
            return True


    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 1:
            return True


    # solution from leetcode comments
    def wordBreak3(self, s, wordDict):
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        return ok[-1]


    # solution from leetcode comments
    def wordBreak4(self, s, wordDict):
        ok = [True]
        max_len = max(map(len,wordDict+[''])) # max len of word in dictionary
        wordDict = set(wordDict)
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(max(0, i-max_len),i)),
        return ok[-1]


s = Solution()
print(s.wordBreak4(s = "aaaaaaa", wordDict = ["aaa","aaaa"]))
# %%

# %%
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)

# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

tup_list = [(x,x*x) for x in range(1,11)]
print("tup_list")
print(tup_list)

# %%
def decorate(func):
    print(func.x)
    print(func)

# %%

@decorate
def foo(x):
  return x +x


foo(3)