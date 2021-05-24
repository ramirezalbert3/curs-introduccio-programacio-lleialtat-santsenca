tenim_electricitat = True
temperatura = 28
manual = False

if tenim_electricitat and (temperatura > 26 or manual):
    aire_acondicionat = True
    print("Engegant l'aire acondicionat")
else:
    aire_acondicionat = False
    print("Aturant l'aire acondicionat, hem d'estalviar energia!")
