n1 = float(input("Dona'm un numero? "))
n2 = float(input("Dona-me'n un altre? "))
op = input("Una operacio? ")

if op == "+":
    print(n1, op, n2, "=", n1+n2)
if op == "-":
    print(n1, op, n2, "=", n1-n2)
if op == "*":
    print(n1, op, n2, "=", n1*n2)
if op == "/":
    print(n1, op, n2, "=", n1/n2)


# alternativa utilitzant elif
# que es una combinacio de else + if
#
# if op == "+":
#     print(n1, op, n2, "=", n1+n2)
# elif op == "-":
#     print(n1, op, n2, "=", n1-n2)
# elif op == "*":
#     print(n1, op, n2, "=", n1*n2)
# elif op == "/":
#     print(n1, op, n2, "=", n1/n2)
# else:
#     print("operacio no valida: ", op)
