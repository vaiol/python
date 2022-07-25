# сортування

def remove_duplicates_list(array):
    # O(n**2)
    res_arr = list()
    for n in array: # O(n)
        if n not in res_arr: # O(n)
            res_arr.append(n)
    return res_arr






def remove_duplicates_set(array):
    set_from_arr = set(array)           # O(n)
    list_from_set = list(set_from_arr)  # O(n)
    return sorted(list_from_set)        # O(n log(n))




def remove_duplicates(nums):
    # O(n) solution
    j = 0
    for i in range(len(nums)):
        if(i < len(nums) - 1 and nums[i] == nums[i + 1]):
            continue
        nums[j] = nums[i]
        j += 1
    return nums[:j]



print(remove_duplicates([1,1,2]))              #[1,2]
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))#[0,1,2,3,4]
print(remove_duplicates([1,1,1,1,1,1,1,1]))    #[1]