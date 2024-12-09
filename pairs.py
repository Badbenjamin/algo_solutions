
#  O(n*2) solution (two loops)
def pairs(k, arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] - arr[j] == k:
                count += 1
    return count

#  O(1) using HASHMAP and SORTED ARRAY

# target 2, arr = [1,5,3,4,2]
# we need to check if the current number is a "diff" that has been stored in hashmap
# "diff" is current number + target, since ex(3-1=2 or 2+1=3) 3 is current num, but also diff
# [1,5,3,4,2] = arr
# [3,7,5,6,4] = diffs (num + target(2))
# iterate through arr, checking hash map for diffs

# ARRAY SHOULD BE SORTED
# BECAUSE WE ARE ALWAYS LOOKIND BACK INTO HASHMAP OF PREV DIFFS AND COMPARING TO CURRENT


def pairs(k, arr):
    new_arr = sorted(arr)
    prev_map = {}
    count = 0
    for i in range(len(new_arr)):
        diff = new_arr[i] + k
        cur_num = new_arr[i]
        # in operator checks if KEY EXISTS
        if (cur_num in prev_map):
            count += 1
        prev_map[diff] = i
    print(prev_map)
    return count

print(pairs(2, [1,5,3,4,2]))
print(pairs(6, [2,8,3,9,7,6,0]))
print(pairs(10, [1,2,3,4,5]))

