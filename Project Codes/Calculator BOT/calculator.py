
def calculate(string, int1, int2):
    
    result = 0
    
    if string == "add":
        result = int1 + int2
    elif string == "subtract":
        result = int1 - int2
    elif string == "multiply":
        result = int1 * int2
    elif string == "divide":
        result = int1 / int2
    else:
        return ("Unknown Argument")
    
    return (result)