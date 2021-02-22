from typing import List

class MoveZeroes:
    def move_zeroes(self, nums: List[int]):
        count=0
        new_arr=[]
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
        for i in range(len(nums)):
            if nums[i]!=0:
                new_arr.append(nums[i])
        for i in range(count):
            new_arr.append(0)
        nums= new_arr
        print(nums)

arr=[0,1,0,3,12]
move_zero= MoveZeroes()
move_zero.move_zeroes(arr)