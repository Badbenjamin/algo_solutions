tc1 = ["red", "red", "blue", "green", "red", "red"]
tc2 = [1, "1", "3", "4", 5, "5", "3", 3,  "fukk"]
tc3 = ["1", "1", "1" , "2", "2", "2", "3"]

# grab a string from strings[i], set as current
# add current to result if current not in result (or if result is empty array)

def not_in_place_mixed(strs):
    result = []
    for s in strs:
        current = str(s)
        if result == [] or current not in result:
            result.append(current)
    return result

# print(not_in_place_mixed(tc2))

# in place

# grab strings[i], set to current
# excluding current, pop strings == current
# how do I stay in bounds?
# THIS WAS MY ATTEMPT
# the problem was that the for loops keep iterating as the string gets shorter, skipping the element that falls into place after the pop
# the solution is to use a while loop which conditionally incriments i and j, so that the index remains the same after the pop
def in_place_mixed(strs):
    length = len(strs)
    for i in range(length):
        if i < length:
            current = strs[i]
            print("cur", current)
        else:
            print(strs)
        for j in range(length):
            if (i + 1) + j < length:
                c2 = strs[(i + 1) + j]
                print("c2", c2)
                if current == c2:
                    strs.pop((i + 1) + j)
                    print("pop")
                    length = len(strs)
    print(strs)


# in_place_mixed(tc1)

# this answer is O(1) because it just has one loop that checks the pointer against a slice of the array
# What is the memory complexity? 
def gpt_answr(strs):
    index = 0
    # stay in bounds with while loop that only runs while the index is less than the length of the string
    while index < len(strs):
        # strs[:index] is a slice of the list up until the index
        # if strs[index] (current) is in the slice (everything up until the index, not including), then the index is popped
        # but the index stays the same so it will not skip over another number, it will just check the next index against the slice
        if strs[index] in strs[:index]:
            strs.pop(index)
        else:
            index += 1
    print(strs)  

print(tc1)
gpt_answr(tc1)

# STACK OVERFLOW ANSWER

def remove_dup(strs):
    i = 0
    # be careful when using for loops and modifying them while iterating through
    # while loop is better because you stay in bounds
    while i < len(strs):
        # j, pointer 2, is one ahead of i 
        j = i + 1
        # while j in bounds, run this loop
        while j < len(strs):
            # if strs[i] and strs[j] are the same, delete strs[j]
            # j incriments and all identical chars will be deleted
            if strs[i] == strs[j]:
                strs.pop(j)
            # when a char that does not match i is encountered, incriment j
            else:
                j += 1
        # once duplicates of i have been removed, i is incrimented to the next index
        i += 1
    print(strs)

# remove_dup(tc3)


# this is better than my origional for loop function
# the index does not automatically advance
# while deletions are happening, the index stays the same
def remove_dup_ben(strs):
    i = 0
    while i < len(strs):
        j = i + 1
        while j < len(strs):
            # j does not advance, next element falls back to j after pop
            if str(strs[i]) == str(strs[j]):
                strs.pop(j)
            # index j only advances if strs[j] does not match strs[i]
            else:
                j += 1
        # once j has incrimented to be equal to the length of the string, leave while loop and incriment i to next str
        i += 1
    print(strs)

# remove_dup_ben(tc3)