import sys



if len(sys.argv) != 4:
    print('Arg len should be 4')
    sys.exit()

# +, -, /, *

# ['L3/src/calculate.py', '2', '+', '2']
# [лівий операнд] [ариф опер] [правий опера]

# PEP-8
left_operand = sys.argv[1]
right_operand = sys.argv[3]

operation = sys.argv[2]

allowed_operations = ['+', '-', '/', '*']

if operation not in allowed_operations:
    print('Operation is not allowed')
    sys.exit()
try:
    left_operand = int(left_operand)
    right_operand = int(right_operand)
except ValueError:
    print('Left and Right operands must be int')
    sys.exit()

if operation == '/' and right_operand == 0:
    print('Division by zero is not allowed')
    sys.exit()

## Option 1
# if operation == '*':
#     print(left_operand * right_operand)
# elif operation == '+':
#     print(left_operand + right_operand)

## Option 2
# match operation:
#     case '*':
#         print(left_operand * right_operand)
#     case '+':
#         print(left_operand + right_operand)


## Option 3
# print(eval(f'{left_operand}{operation}{right_operand}'))


# def perform_operation(left, right, operation)
#     return ()


    





