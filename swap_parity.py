
# re arrange all numbers in an int but only swapping odds for odds and evens for evens to create the largest number

# O(N)
# pretty self explanitory
# create lists of odd numbers and even numbers separately
# sort lists (sm to lg)
# iterate through source number
# if even, add digit from end of even list (popped value)
# if odd, add digit from end of odd list

def largestInteger(self, num):
        odd_arr = []
        even_arr = []
        for dig in str(num):
            if int(dig) % 2 == 0:
                even_arr.append(int(dig))
            else:
                odd_arr.append(int(dig))

        sorted_odd = sorted(odd_arr)
        sorted_even = sorted(even_arr)
        
        result = ""
        for dig in str(num):
            if int(dig) % 2 == 0:
                result += str(sorted_even.pop())
            else:
                result += str(sorted_odd.pop())
        return (int(result))