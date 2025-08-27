class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def robber(nums):
            if len(nums)==1:
                return nums[0]
            dp=[0]*len(nums)
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i]=max(nums[i]+dp[i-2],dp[i-1])
            return dp[-1]
        nums1=nums[1:len(nums)]
        nums2=nums[0:-1]
        m1=robber(nums1)
        m2=robber(nums2)
        return max(m1,m2)
