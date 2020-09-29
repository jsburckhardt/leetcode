# class Solution:
def twoSum(nums, target):
    x = 0
    nums_base = nums[:]
    nums.sort()
    while x < len(nums)-1:
        y = x+1
        limit = target - nums[x]
        if nums[y] > limit:
            break
        while y < len(nums):
            if nums[x] + nums[y] == target:
                result = []
                result.append(nums_base.index(nums[x]))
                if nums_base.index(nums[x]) == nums_base.index(nums[y]):
                    result.append(nums_base[nums_base.index(
                        nums[x])+1:].index(nums[x]) + nums_base.index(nums[x])+1)
                else:
                    result.append(nums_base.index(nums[y]))
                if result[0] > result[1]:
                    result[0], result[1] = result[1], result[0]
                return result            
            y = y+1
        x = x + 1

nums = [-3,4,3,90]
target = 0
print(f"{twoSum(nums,target)}")
