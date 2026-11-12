class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        m = 1
        mult = []
        for i in nums:
            m *= i
            left.append(m)
        m = 1
        for i in reversed(nums):
            m *= i
            right.append(m)
        right = right[::-1]
        result = []
        for i in range(len(nums)):
            l = r = 1
            if i - 1 >= 0:
                l = left[i-1]
            if i + 1 < len(nums):
                r = right[i+1]
            result.append(l*r)
        return result
