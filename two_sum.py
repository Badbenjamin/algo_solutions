a1 = [1,2,3,5]
a2 = [4,3,7,6]
a3 = [1,2,3,4,5,6]

# O(n) solution, returns indicies
def two_sum(arr, target):
    for i in range(len(arr)):
        p1 = arr[i]
        j = i + 1
        while j < len(arr):
            p2 = arr[j]
            if p1 + p2 == target:
                return [i,j]
            else:
                j += 1
    return []



# print(two_sum(a1, 5))
# print(two_sum(a2, 7))

# 0(n) HASHMAP SOLUTION
# we are looking for the DIFF as we iterate, and saving the NUM if we don't find a match
# if x + y = target, then target - x = y. target - x = DIFF
# if the target - current num is a previous num, return the inicies of both
# else, add current num to previous nums hashmap


def two_sum_hash(arr, target):
    prev_map = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[num] = i 
        print(prev_map)

print(two_sum_hash(a3, 10))

# SORTING )(n log n)

def two_sum_sort(arr, target )

