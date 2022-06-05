'''
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.
You may assume that each input would have exactly one solution, and you may not
use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class TwoSums:
    @staticmethod
    def get_twosums_2loops (arr , out):
        for i in range(0, len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i]+arr[j] == out:
                    return i, j

        return -1,-1

    # above solution is with 2 for loop.

    @staticmethod
    def get_twosum_enumrate(nums,target):
        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums :
                return (i,nums.index(x))
            else:
                continue

        return -1,-1


arr = list(map(int,input().split()))
print(f'list: {arr}')
out=int(input())
print(f"sum value:{out}")
#a,b = TwoSums.get_twosums_2loops(arr,out)
#print(a,b)
a,b=TwoSums.get_twosum_enumrate(arr,out)
print(a,b)


