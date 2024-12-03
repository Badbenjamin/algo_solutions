a1 = ["flow", "flower", "flight"]
a2 = ["aa", "ac", "ab"]

def longest_prefix(arr):
    result = []
    # loop over all the characters in the first string of array
    # a prefix cannot be longer than the shortest string
    for i in range(len(arr[0])):
        # p1 is the character in the first string
        pointer_one = arr[0][i]
        for str in arr:
            # p2 is the [i]th char of each string in the array
            pointer_two = str[i]
            # if i is the same as the lenght of the current string, return
            # it has reached the end and cannot continue, 
            # if p1 and p2 don't match, then the char must be different, return
            if i == len(str) or pointer_two != pointer_one:
                return result
        # if p1 matches p2 in every string and is not yet out of range on each string, append to result
        result.append(pointer_one)
    return result


print(longest_prefix(a2))