class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cout=[]
        for i in range(len(nums)):
            ctr=0
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:
                    ctr+=1
            cout.append(ctr)
        return cout
            
