
def interpret(input):
    i = 0
    j = 0
    k = 0
    output = [0]
    result = []
    while i in range(len(input)):
        if input[i] == "+":
            output[j] += 1
        elif input[i] == "-":
            output[j] -= 1
        elif input[i] == ">":
            j += 1
            if j not in range(len(output)):
                output.append(0)
        elif input[i] == "<":
            j -= 1
            if j not in range(len(output)):
                print("Acess out of range")
                return None
        elif input[i] == "[" and output[j] == 0:
            while i in range(len(input)) and not input[i] == "]":
                i += 1
        elif input[i] == "]" and not output[j] == 0:
            while i in range(len(input)) and not input[i] == "[":
                i -= 1 
        elif input[i] == ".":
            result.append(output[j])
        elif input[i] == ",":
            output[j] = input("Enter an integer: ")
        else:
            pass
        i += 1
    return result

if __name__ == "__main__":
    print(interpret("++++++++++[>+++++++>++++++++++>+++++++++++>+++>+<<<<<-]>++.>>+.---.<---.>>++.<+.++++++++.-------.<+++.>+.>+.>."))
        