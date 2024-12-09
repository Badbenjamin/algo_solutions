    # 
    
    new_arr = [*arr]
    
    for  i in range(len(arr)):
        if arr[k]:
            for i in range(len(new_arr)-1):
                first = new_arr[i][k]
                second = new_arr[i+1][k]
                temp = []
                if first > second:
                    temp = new_arr[i]
                    new_arr[i] = new_arr[i + 1]
                    new_arr[i+1] = temp
    
    for row in new_arr:
        output_line = ""
        for num in row:
            output_line += str(num) + " "
        print(output_line)