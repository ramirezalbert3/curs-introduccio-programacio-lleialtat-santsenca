temp = float(input("Quina temperatura fa? "))

if temp > 26:
    aire_acondicionat = True
    print("Engegant l'aire acondicionat")
else:
    aire_acondicionat = False
    print("Aturant l'aire acondicionat, hem d'estalviar energia!")


tinc = input("Tens bitllet? ")
if tinc == "si":
    porta_oberta = True
    print("Porta oberta, bon viatge!")
else:
    porta_oberta = False
    print("Per favor, compra un bitllet nou a la maquina")


# else es opcional
if tinc != "si":
    print("no tens bitllet!")


print("temp > 26:", temp > 26)
print("temp <= 26:", temp <= 26)
print("tinc == \"si\":", tinc == "si")
print("tinc != \"si\":", tinc != "si")
