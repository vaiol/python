from ast import operator
import sys

ALLOWED_OPERATIONS = ['+', '-', '/', '*', '%']

def calc(left_operand, right_operand, operation):
    # validate operation
    
    if operation not in ALLOWED_OPERATIONS:
        print('Operation is not allowed')
        return None

    # validate operands
    try:
        left_operand = int(left_operand)
        right_operand = int(right_operand)
    except ValueError:
        print('Left and Right operands must be int')
        return None
    
    # validate division by zero
    if operation in ['/', '%'] and right_operand == 0:
        print('Division by zero is not allowed')
        return None

    match operation:
        case '*':
            return left_operand * right_operand
        case '+':
            return left_operand + right_operand
        case '-':
            return left_operand - right_operand
        case '/':
            return left_operand / right_operand
        case '%':
            return left_operand % right_operand
        case _:
            print('Operation is not supported.')
            return None
    

def calculate_4_args():
    left_operand = sys.argv[1]
    right_operand = sys.argv[3]
    operation = sys.argv[2]

    # perform calculation
    result = calc(left_operand, right_operand, operation)

    if result == None:
        # some errors which were printed
        return

    #print result
    print(result)
    
def calculate_2_args(): 
    left_operand, right_operand, operation = '', '', ''
    for op in ALLOWED_OPERATIONS:
        args_arr = sys.argv[1].split(op)
        if len(args_arr) == 2:
            operation = op
            left_operand = args_arr[0]
            right_operand = args_arr[1]
            break

    # perform calculation
    result = calc(left_operand, right_operand, operation)

    if result == None:
        # some errors which were printed
        return

    #print result
    print(result)

args_len = len(sys.argv)
if args_len == 2:
    calculate_2_args()
elif args_len == 4:
    calculate_4_args()
else:
    print('Not allowed number of arguments. Allowed 1 and 3 (combined and separated)')

    





