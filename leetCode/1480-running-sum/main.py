'''
@file           solution.py
@author         morgan bergen
@date           jan 3 2022
@brief          given an array nums
                we define a running sum of an array as runningSum[i] = sum(nums[0]...nums[i])
                return the running sum of nums
@description
                example 1
                input           nums = [1, 2, 3, 4]
                output          [1, 3, 6, 10]
                explaination    running sum is obtained as follows 
                                [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]


Think about how we can calculate the i-th number in the running sum from the (i-1)-th number.
'''

def runningSum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        print(f'{nums} at index {i} {nums[i]} += {nums[i-1]}')
        nums[i] += nums[i - 1]
    return nums

def main():
    nums = [1, 2, 3, 4]
    print(runningSum(nums))
    print(runningSum1(nums))

if __name__ == "__main__":
    main()












































'''    
    @pre    nums is a list of integers
    @param  self is a reference to the current instance of the class
            nums is a list of integers
    @post   returns a list of integers -> List[int] is the return type and is synomymous with Return (List[int])
    @return List[int]

    
    # -> list[int] is a type hint for the return value of runningSum
    # (nums: list[int]) is a data type hint for the argument nums
    def runningSum(self, nums: List[int]) -> List[int]:
'''     
