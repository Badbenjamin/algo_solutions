a1 = ["flow", "flower", "flight"]
a2 = ["aa", "ac", "ab"]
a3 = ["bbb", "bbb", "bbbbbb"]


# this function works by looping through the chars of the first string in the array
# it then checks the first character of the first string against the first character of all strings
# if the characters match, then the character is added to the result string
# if they do not match, or reach the end of the string, then the result returns
def longest_prefix(arr):
    result = ""
    # loop over all the characters in the first string of array
    # a prefix cannot be longer than the shortest string
    for i in range(len(arr[0])):
        # p1 is the character in the first string
        pointer_one = arr[0][i]
        for str in arr:
            # p2 is the [i]th char of each string in the array
            pointer_two = str[i]
            # if i is the same as the lenght of the current string, return
            # it has reached the end and cannot continue, a prefix can't be longer than the shortest string
            # if p1 and p2 don't match, then the char must be different, return
            if i == len(str) or pointer_two != pointer_one:
                return result
        # if p1 matches p2 in every string and is not yet out of range on each string, append to result
        result += pointer_one
    return result


print(longest_prefix(a3))