# value and reference

def double_zero(array):
    res_arr = list(array)
    i = 0
    while(i < len(res_arr)):
        if res_arr[i] == 0:
            res_arr.insert(i + 1, 0)
            i += 1
        i += 1
    return res_arr

def double_zero_1(array):
    res_arr = list()
    for item in array:
        if item == 0:
            res_arr.append(item)
            res_arr.append(item)
        else:
            res_arr.append(item)
    return res_arr


print(double_zero_1([1,0,2,3,0,4,5,0])) # [1,0,0,2,3,0,0,4,5,0,0]
print(double_zero_1([1,0,2,3,0,4,5,0])) # [1,0,0,2,3,0,0,4,5,0,0]
print(double_zero_1([1,2,3])) # [1,2,3]