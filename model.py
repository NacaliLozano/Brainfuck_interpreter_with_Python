import sys

def get_int():
    """Gets a strin from keyboard and returns it in int if it is a number."""
    string = input("Enter a natural number: ")
    if string.isnumeric() or string.startswith("-") and string[1:].isnumeric():
        return int(string)
    else:
        return get_int()
    
def int_to_ascii(feed):
    """Turns a list of int into a string."""
    if feed is None:
        return None
    result = ""
    for i in range(len(feed)):
        result += chr(feed[i])
    return result

def interpret(feed):
    """Turns Brainfuck code into a list of ints."""
    i = 0
    j = 0
    output = [0]
    result = []
    while i in range(len(feed)):
        if feed[i] == "+":
            output[j] += 1
        elif feed[i] == "-":
            output[j] -= 1
        elif feed[i] == ">":
            j += 1
            if j not in range(len(output)):
                output.append(0)
        elif feed[i] == "<":
            j -= 1
            if j not in range(len(output)):
                print("Memory pointer access out of range")
                return None
        elif feed[i] == "[" and output[j] == 0:
            while i in range(len(feed)) and not feed[i] == "]":
                if i == len(feed) - 1:
                    print("No ] detected to the right of [")
                    return None
                i += 1
        elif feed[i] == "]" and not output[j] == 0:
            while i in range(len(feed)) and not feed[i] == "[":
                if i == 0:
                    print("No [ detected to the left of ]")
                    return None
                i -= 1
        elif feed[i] == ".":
            result.append(output[j])
        elif feed[i] == ",":
            output[j] = get_int()
        else:
            pass
        i += 1
    return result

if __name__ == "__main__":
    
    with open(sys.argv[1]) as f:
        code = f.readlines()
    br_code_string = ""
    for line in code:
        br_code_string += line
    
    int_list = interpret(br_code_string)
    print("int_list: " + int_list)
    string = int_to_ascii(int_list)
    print("string: " + string)
    

    
    #print(int_to_ascii(interpret("+++++.+++++[+++++")))
        