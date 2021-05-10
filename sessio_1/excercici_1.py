# 1+2
# print('Hola mon')
# 'onze'*4

# print(1+2)
# print('Hola mon')
# print('onze'*4)

# num = input("Quin numero vols multiplicar per 7? ")
# print(num*7)

# PROGRAMA RENCOROS

qui = input("Qui m'ha dit una mentida? ")

rencor = {
    "clara": True,
    "alba": False,
    "albert": True,
    "alfred": False
}
print(qui, "t'ha dit una mentida:", rencor[qui])

rencor = {
    "clara": 0,
    "alba": 3,
    "albert": 0,
    "alfred": 17
}
print(qui, "t'ha dit", rencor[qui], "mentides")

rencor = {
    "clara": [],
    "alba": [3, 8, 21],
    "albert": [],
    "alfred": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
}
print(qui, "t'ha dit mentides els dies:", rencor[qui])
