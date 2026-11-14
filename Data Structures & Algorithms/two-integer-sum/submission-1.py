class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            j = i + 1
            while j < n:
                if nums[i] + nums[j] == target:
                    return [i,j]  
                j += 1         