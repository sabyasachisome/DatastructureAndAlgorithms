from typing import List
import logging

logging.basicConfig(level=logging.DEBUG)

class Solution:
    def get_left_element(self,nums,target,left,right):
        while left<=right:
            mid= (left+right)//2
            logging.info('mid= {}'.format(mid))
            if nums[mid]==target:
                logging.info('{} {} {}'.format(mid, nums[mid],target))
                if ((mid-1>=0 and nums[mid-1]!=target) or mid==0):
                    logging.info('inside second')
                    return mid
                right= mid-1
            elif nums[mid]>target:
                right= mid-1
            else:
                left=mid+1
        return -1

    def get_right_element(self,nums,target,left,right):
        while left<=right:
            mid= (left+right)//2
            if nums[mid]==target:
                if ((mid+1<len(nums) and nums[mid+1]!=target) or mid==len(nums)-1):
                    return mid
                left=mid+1
            elif nums[mid]>target:
                right= mid-1
            else:
                left=mid+1
        return -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left= 0
        right= len(nums)-1
        left_element= self.get_left_element(nums,target,left,right)
        right_element = self.get_right_element(nums, target,left,right)
        return (left_element,right_element)

if __name__ == '__main__':
    nums = [1, 4]
    target = 4
    sol= Solution()
    print(sol.searchRange(nums, target))
