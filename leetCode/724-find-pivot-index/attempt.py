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


@hint       Create an array sumLeft where sumLeft[i] is the sum of all the numbers to the left of index i

'''

def print_list(p_nums: list[int]) -> None:

    print("[", end="")
    for i in reversed(range(len(p_nums))):
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
    print_list(nums)

    # find the sum of the entire list
    sum = 0
    for i in range(len(nums) - 1):
        sum += nums[i]
        if i == (len(nums) - 2):
            print((nums[i]), end=" = ")
        else:
            print((nums[i]), end=" + ")
    print(sum)
    
    left = []
    right = []
   
    for i in range(len(nums)):  
        if len(left) == sum:
            return(i)    
        else:
            left.append(nums[i])
            pass

        for i in range(reversed(len(nums)/2)):
            right.append(nums[i])

    return(len(nums))

def main():
    example = [1,7,3,6,5,6]
    print(f'{example}')
    print(f'{pivotIndex(example)}')

    for i, v in enumerate(example):
        print(f'{i} {v}')

    # explain this syntax
    # for i, v in enumerate(example):
    #     print(f'{i} {v}')
    
    '''
    this means for each index i and value v in the list example iterate through the list
    i is initialized to 0 and v is initialized to the first value in the list
    for i, v enumerate(example):
    '''

if __name__ == "__main__":
    main()


















































