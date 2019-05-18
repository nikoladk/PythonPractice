def calc(a, b, op):

    operators = '+-*/'
    if op not in operators:
        return 'Please select ono of these characters: "+, -, *, /"!'


    if op == '+':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b)
    if op == '-':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
    if op == '/':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)
    if op == '*':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)


def main():
    a = int(input('Please type first number: '))
    b = int(input('Please type second number: '))
    op = input('Please select operation symbol, choose between: "+, -, /, *" ')

    print(calc(a, b, op))


if __name__ == '__main__':
    main()