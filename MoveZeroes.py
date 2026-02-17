class Solution(object):
    def moveZeroes(self, nums):
        writepos=0
        for readpos in range(len(nums)):
            if nums[readpos] != 0:
                if readpos != writepos:
                    nums[readpos],nums[writepos]=nums[writepos],nums[readpos]
                writepos += 1
        
