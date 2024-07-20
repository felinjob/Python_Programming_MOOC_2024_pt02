
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    elif len(my_string) == 1:
        return False
    
    my_string = "".join([character for character in my_string if character in "()[]"])
    if my_string[0] == '(':
        if not (my_string[0] == '(' and my_string[-1] == ')'):
            return False
    elif my_string[0] == '[':
        if not (my_string[0] == '[' and my_string[-1] == ']'):
            return False
        
    # remove first and last character
    return balanced_brackets(my_string[1:-1])


if __name__ == "__main__":
    print(balanced_brackets())