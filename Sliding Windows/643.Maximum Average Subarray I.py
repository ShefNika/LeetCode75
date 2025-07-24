class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        sum_ = max_sum
        for i in range(k,len(nums)):
            sum_ += nums[i] - nums[i - k]
            if max_sum < sum_:
                max_sum = sum_
        return max_sum/k
