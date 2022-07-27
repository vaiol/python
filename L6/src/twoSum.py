from typing import List




def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]





def twoSumDict(nums: List[int], target: int) -> List[int]:
    hashmap = dict()
    for i in range(len(nums)):
        currVal = target - nums[i]
        if currVal in hashmap:
            return [i, hashmap[currVal]]
        hashmap[nums[i]] = i