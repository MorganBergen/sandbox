'''
@file           main.py
@author         morgan bergen
@date           jan 5 2022
@brief          leetcode 724 find pivot index
@description    given an array of integers nums, calculate the pivot index of this array.  the pivot index is the index where the sum of all the numbers strictly to the left of the index is ewqual to the sum of all the numbers strictly to the index's right.  If the index is on the left edge of the array, then the left sum of 0, because there are no elements to the left.  this also applied to the right edge of the array.  return the leftmost pivot index.  if no sych index exists, return -1
'''

def pivotIndex(nums: list[int]) -> int:
    sum = 0
    for i in nums:
        sum += i

    # find the pivot index
    leftSum = 0
    for i in range(len(nums)):
        if leftSum == sum - leftSum - nums[i]:
            return i
        leftSum += nums[i]

    return -1


def main():
    '''
    @brief      main function
    @return     none
    '''
    nums = [1, 7, 3, 6, 5, 6]
    print(pivotIndex(nums))

if __name__ == '__main__':
    main()
