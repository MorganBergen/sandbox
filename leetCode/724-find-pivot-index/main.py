'''
@file       main.py
@author     morgan bergen
@date       jan 3 2022
@brief      leetcode 724 find pivot index

@details    given an array of integers <nums>, calculate the pivot index of this array.
            the pivot index is the index where the sum of all the numbers 
            strictly to the left of the index is equal to the sum of all the numbers strictly to right of the index
             
            if the pivot index is on the left edge of the array, 
            then the left sum is 0, because there are no elements to the left
            
            if the pivot index is on the right edge of the array, 
            then the right sum is 0, because there are no elements to the right
            
            return the leftmost pivot index, if no such index exists, return -1

                                             ↓ 
@example    input           nums = [1, 7, 3, 6, 5, 6]
            output          3
            explaination    the pivot index is 3
                            left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
                            right sum = nums[4] + nums[5] = 5 + 6 = 11

                                    ↓
@example    input           nums = [2, 1, -1]
            output          0
            explaination    the pivot index is 0


@example    input           nums = [1,2,3]
            output          -1
            explaination    there is no index that satisfies the conditions in the problem statement


'''

def print_list(p_nums: list[int]) -> None:

    print("[", end="")
    for i in reversed(range(len(nums))):
        if (i != 0):
            print(p_nums[i], end=", ")
        else:
            print(p_nums[i], end="")
    print("]", end="\n")


    print("[", end="")
    for i in range(len(p_nums)):
        if (i != len(p_nums) - 1):
            print(p_nums[i], end=", ")
        else:
            print(p_nums[i], end="")
    print("]", end="\n")

def pivotIndex(nums: list[int]) -> int:
  
    print_list(p_nums)

    return(len(nums))

def main():
    example = [1,7,3,6,5,6]
    print(f'{example}')
    print(f'{pivotIndex(example)}')


if __name__ == "__main__":
    main()



















































