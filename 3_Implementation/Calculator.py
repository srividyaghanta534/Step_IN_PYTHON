# Declaration of global variables
global number_of_operations
global result
number_of_operations = 0
result = 0

''' @brief: Function to print the final result
    @input: None
    @output: None 
'''

def printResult():
    global result
    print("the final result is:")
    print(result)
    exit(0)

''' @brief: Function to perform Multipication operation
    @input: None
    @output: None 
'''

def performMultiplication():
    global result
    if number_of_operations == 0:
        print("Enter two operands")
        operand1, operand2 = [int(x) for x in input().split()]
        result = operand1 * operand2
    else:
        print("Enter operand")
        operand = int(input())
        result *= operand
    return

''' @brief: Function to perform Integer Division operation
    @input: None
    @output: None 
'''

def performIntegerDivision():
    global result
    if number_of_operations == 0:
        print("Enter two operands")
        operand1, operand2 = [int(x) for x in input().split()]
        result = operand1 // operand2
    else:
        print("Ebter the operand")
        operand = int(input())
        result //= operand
    return

''' @brief: Function to perform float division operation
    @input: None
    @output: None 
'''

def performFloatDivision():
    global result
    if number_of_operations == 0:
        print("Enter two operands")
        operand1, operand2 = [int(x) for x in input().split()]
        result = operand1 / operand2
    else:
        print("Enter the operand")
        operand = int(input())
        result /= operand
    return

''' @brief: Function to perform subtraction operation
    @input: None
    @output: None 
'''

def performSubtraction():
    global result
    if number_of_operations == 0:
        print("enter two operands")
        operand1, operand2 = [int(x) for x in input().split()]
        result = operand1 - operand2
    else:
        print("Enter the operand")
        operand = int(input())
        result -= operand
    return

''' @brief: Function to perform addition operation
    @input: None
    @output: None 
'''

def performAddition():
    global result
    if number_of_operations == 0:
        print("Enter two operands")
        operand1, operand2 = [int(x) for x in input().split()]
        result = operand1 + operand2
    else:
        print("Enter the operand")
        operand = int(input())
        result += operand
    return

''' @brief: Function to determinte the arithemetic operation to perform
    @input: None
    @output: None 
'''

def operation():
    global number_of_operations
    operator = input("Enter the operator")
    if operator == '+':
        performAddition() 
    elif operator == '-':
        performSubtraction()
    elif operator == '/':
        performFloatDivision()
    elif operator == '//':
        performIntegerDivision()
    elif operator == '*':
        performMultiplication()
    elif operator == '=':
        printResult()
    number_of_operations += 1
    return

''' @brief: Main function to execute until True
    @input: None
    @output: None 
'''

def main():
    while(True):
        operation()

if __name__ == "__main__":
    main()
