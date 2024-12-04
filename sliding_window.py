# SUBSTRING COUNT

def count_substring(string, sub_string):
    k = len(sub_string)
    
    count = 0
    # Why k-1? because j is k + i
    # SPEND A LITTLE MORE TIME ON THIS FIGURING IT OUT
    print(range(len(string)-(k - 1)))
    for i in range(len(string)-(k - 1)):
        window = []
        for j in range(k):
            window.append(string[i+j])
        if "".join(window) == sub_string:
            count += 1
    return count

# print(count_substring("ABCDCDC", "CDC"))
# print(count_substring("aabbccaabbccaa", "aa"))
# count_substring("1234567","12")

# WITH STEP SIZE OF K

def sliding_window_step(string, k):
   # create sliding window of k size (iterate over range - k size)
   # iterate by size of k (k is step size)
   # use set to de duplicate each chunk of string
   # print each de duplicated substring
  
    window_list = []
    i = 0
    while i < len(string):
        window = []
        for j in range(k):
            window.append(string[i + j])
        window_list.append(list(set(window)))
        i += k
    print(window_list)

sliding_window_step("ssbbbsccfffc", 2)