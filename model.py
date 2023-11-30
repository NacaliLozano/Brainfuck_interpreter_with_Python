import sys

def get_int():
    """Gets a strin from keyboard and returns it in int if it is a number."""
    string = input("Enter an integer: ")
    if string.isnumeric():
        return int(string)
    else:
        return get_int()
    
def int_to_ascii(feed):
    """Turns a list of int into a string."""
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
                print("Acess out of range")
                return None
        elif feed[i] == "[" and output[j] == 0:
            while i in range(len(feed)) and not feed[i] == "]":
                i += 1
        elif feed[i] == "]" and not output[j] == 0:
            while i in range(len(feed)) and not feed[i] == "[":
                i -= 1
        elif feed[i] == ".":
            result.append(output[j])
        elif feed[i] == ",":
            output[j] = get_int()
        else:
            print("Input error.")
            return None
        i += 1
    return result

if __name__ == "__main__":
    
    with open(sys.argv[1]) as f:
        code = f.readlines()
    for line in code:
        print(int_to_ascii(interpret(line)))
        
    
    #print(int_to_ascii(interpret("++++++++++[>+++++++>++++++++++>+++++++++++>+++>+<<<<<-]>++.>>+.---.<---.>>++.<+.++++++++.-------.<+++.>+.>+.>.")))
        