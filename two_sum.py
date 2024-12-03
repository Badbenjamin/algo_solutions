a1 = [1,2,3,5]
a2 = [4,3,7,6]

# O(n) solution
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

print(two_sum(a1, 5))
print(two_sum(a2, 7))