def valid_parens(parens):
    paren_list = []
    # cant be valid if string begins with closing paren
    # cant be valid if uneven
    if parens[0] == ")" or len(parens) % 2 != 0:
        return False
    for paren in parens:
        # add opening paren to stack
        if paren == "(":
            paren_list.append(paren)
        # if stack is not empty (has opening parens), pop opening for every closing
        elif paren == ")" and paren_list != []:
            paren_list.pop()
        # if paren is ) and list is [], return false
        # a closing paren without an open is automatically invalid
        else:
            return False
    if paren_list == []:
        return True
    else:
        return False


print(valid_parens("()"))
print(valid_parens(")("))
print(valid_parens("())"))
print(valid_parens("(()((())))"))
print(valid_parens("()))"))
