from typing import List

class MoveZeroes:
    def move_zeroes(self, nums: List[int]):
        j: int= 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        for i in range(j, len(nums)):
            nums[i]=0

arr=[0,1,0,3,12]
move_zero= MoveZeroes()
move_zero.move_zeroes(arr)