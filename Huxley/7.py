x = float(input())
y = input()
op = input()

while op != '&':

    if op == '+':
        x += float(y)
        print("%.3f" % x)
    elif op == '-':
        x -= float(y)
        print("%.3f" % x)
    elif op == '*':
        x *= float(y)
        print("%.3f" % x)
    elif op == '/':
        if float(y) == 0:
            print("operacao nao pode ser realizada")
        else:
            x /= float(y)
            print("%.3f" % x)

    y = input()
    op = input()
