# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        ml=len(nums)+1
        l=0
        start=0
        for i in nums:
            if i>=target:
                return 1
            s+=i
            l+=1
            if s>=target:
                
                while(s>=target+nums[start] and start<len(nums)):
                    s-=nums[start]
                    start+=1
                    l-=1
                ml=min(l,ml)
        if ml==len(nums)+1:
            return 0
        return ml
