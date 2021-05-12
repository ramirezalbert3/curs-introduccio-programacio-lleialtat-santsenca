paraules = "unes paraules molt boniques"
print(type(paraules))
print(paraules)

print("#"*25)

numeros = 345
print(type(numeros))
print(numeros)

print("#"*25)

decimals = 345.45
print(type(decimals))
print(decimals)

print("#"*25)

llista = [1, 2, "tres", "4"]
print(type(llista))
print(llista)
print(llista[2])

print("#"*25)

diccionari = {
    "primer": 1,
    "segon": 2,
    "tomaquet": "fruita",
}
print(type(diccionari))
print(diccionari)
print(diccionari["segon"])

print("#"*25)

complicat = {
    "paraules": paraules,
    "numeros": numeros,
    "decimals": decimals,
    "llista": llista,
    "diccionari": diccionari,
}
print(type(complicat))
print(complicat)
print(complicat["llista"][2])


# Les linies que comencen amb # son comentaris i no s'executen!

# 1. Podem sumar números decimals amb números enters?
print(1+2.3)
# 2. Podem guardar llistes dins de llistes?
llistes = [[1, 2, 3], [4, 5, 6]]
print(llistes)
# 3. I diccionaris dins de diccionaris?
diccionaris = {"dict": {"un": 1, "dos": 2}}
print(diccionaris)
# 4. I llistes dins de diccionaris i a l'inrevés?
llistadict = [diccionaris]
print(llistadict)
dictllista = {"llistes": llistes}
print(dictllista)
# 5. Podem mirar si dues paraules o números són iguals? Recordatori: `==` (igual) i `!=` (desigual)
print(3 == 3)
print(3 == 4)
print(3 != 3)
print(3 != 4)
print("tres" == "tres")
print("tres" != "tres")
print("tres" == "quatre")
print("tres" != "quatre")
# 6. Podem mirar si dues paraules o números són més grans o més petits que un altre? Pista: `<` i `>`
print(3 > 3)
print(3 > 4)
print(3 < 3)
print(3 < 4)
print("tres" > "tres")
print("tres" < "tres")
print("tres" > "quatre")
print("tres" < "quatre")
# 7. Podem convertir un número a paraula i una paraula a número? Pista: `int("3")`, `float("3.7")`, `str(3.6)`
print(type(int("3")))
print(type(float("3.7")))
print(type(str(3.6)))
# 8. Pot ser que fos això el que li passava al nostre programa que no sabia la taula del 7?
num = float(input("Quin numero vols multiplicar per 7? "))
print(num*7)
# 9. Podem convertir un número decimal a un enter al revés?
print(int(3.7))
print(float(3))
# 10. Què passa quan intentem utiltizar posicions d'una llista que no existeixen? Exemples: `llista[-1]` o `llista[123456]`
llista = [1, 2, 3]
# llista[-1] # EL PROGRAMA FALLA
# llista[3] # EL PROGRAMA FALLA (nomes son valids 0, 1 i 2)
# 11. I quan utiltizem etiquetes que no existeixen en un diccionari? Exemple: `diccionari["no existeix"]`
diccionari = {"un": 1, "dos": 2}
# diccionari["tres"] # EL PROGRAMA FALLA
# 12. Podem utilitzar un número com etiqueta d'un diccionari?
clarquesi = {1: "un", 2: "dos"}
print(clarquesi)
