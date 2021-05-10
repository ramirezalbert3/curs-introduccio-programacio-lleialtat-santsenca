# Introducció a la programació en Python

Els llenguatges de programació ens permeten **comunicar-nos amb els ordinadors** i demanar-los que ens facin qualsevol seguit de tasques.

`Python` es un **llenguatge de programació modern** (dels anys 90) i molt extès a totes les indústries ja que és molt **versàtil** i **senzill**.

Els dissenyadors de `Python` el defineixen com "**el 2n millor llenguatge per a fer qualsevol tasca**", `Python` no és el millor llenguatge per a cap tasca en concret, però permet fer qualsevol tasca que puguis imaginar molt fàcilment.

## On puc trobar Python

`Python` és gratuït i es pot descarregar de la seva web oficial: [https://www.python.org](https://www.python.org)

Per a proves ràpides (si no tens un ordinador amb `Python` instal·lat a mà) pots fer servir: [https://replit.com/languages/python3](https://replit.com/languages/python3)

## Primeres passes

Com es "programa"?

Com "escric" `Python`?

Obre la **terminal** del teu ordinador i escriu-hi `python`, hi veuràs una pantalla molt semblant a això:

```bash
$ python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Fem unes quantes proves!

- Escriu-hi una operació simple com `1+2` i apreta `Enter`
- Demana que "imprimeixi (`print`)" per pantalla: `print('Hola mon!')` i apreta `Enter`

```python
>>> 1 + 2
3
>>> print('Hola mon!')
Hola mon!
>>>
```

La terminal de `Python` és **interactiva** i permet anar **evaluant** operacions i tasques en directe.
Investiga una mica més, prova diverses operacions aviam què en surt. No tinguis por, si una operació no es correcta `Python` es queixarà una mica, però **seguirà corrent**.

### Exercicis d'operacions

- Es poden sumar dues paraules?
- Es poden sumar un número i una paraula?
- Són necessàries les cometes al voltant de les paraules?
- Es poden fer altres operacions amb números? (pista: els operadors bàsics són `+` `-` `*` `/`)
- Es poden multiplicar paraules?

```python
>>> "hola" + "mon"
'holamon'
>>> "tres es " + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> hola
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hola' is not defined
>>> 3*7
21
>>> 3/7
0.42857142857142855
>>> "onze"*3
'onzeonzeonze'
>>> 
```

Ja veus que `Python` és bastant intuïtiu, i també és bastant evident quan alguna cosa no li ha agradat.

Per a sortir de la terminal de `Python` apreta `Ctrl+C` o `Ctrl+D`, depenent de si l'ordinador és Windows o Linux.

```python
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
usuari@ordinador sessio_1 %
```

## Organitzant el codi

Treballar amb la terminal de `Python` pot ser força útil, però els ordinadors "funcionen sols", no hi ha una persona enganxada a l'ordinador escrivint-hi operacions. Com es fa això?

Les operacions i **tasques** es deixen escrites en **fitxers de text** per a que l'**ordinador els llegeixi i els processi**.

Cada llenguatge de programació té la seva pròpia **convenció sobre com es diuen i com s'estructuren aquests arxius**, però per sort `Python` és dels més senzills de tots.

Crea un arxiu de text amb el nom `prova.py`.

Ara obre aquest arxiu i escriu-hi unes quantes operacions:

```python
1+2
print('Hola mon')
'onze'*4
```

Guarda'l i, per **executar-lo**, des del terminal escriu: `python prova.py`. Així és com "demanem" a `Python` que **executi el nostre codi**.

```bash
usuari@ordinador sessio_1 % python prova.py 
Hola mon
```

Sembla que tot ha anat "bé", però potser no del tot bé, no sembla que ho hagi executat tot no?
Sembla que només ens ha **ensenyat per pantalla** allò que hem fet `print()`? Provem de fer print de tot.

```python
print(1+2)
print('Hola mon')
print('onze'*4)
```

Guardem l'arxiu i tornem a executar-lo (escrivint al terminal: `python prova.py`).

```bash
usuari@ordinador sessio_1 % python prova.py 
3
Hola mon
onzeonzeonzeonze
```

Aaaaaara sembla que si. Sembla que si que **ho executava tot**, però quan "executes un fitxer de `Python`" has de demanar el que vols que et mostri per pantalla amb `print`.

## TODO:

## Variables

Ara parlarem de la peça més bàsica de la programació, la **variable**. Una variable és simplement un nom que li donem a un valor per a no haver de repetir-lo tota l'estona. Obre python, escriu `hola = "Hola! M'agradaria saludar a: "` i apreta Enter, sembla que no ha fet res?

```python
>>> hola = "Hola! M'agradaria saludar a: "
>>> 
```

Alguna cosa haurà fet segurament, anem a provar coses com `hola + "Clara"` o `hola + "Albert"`.

```python
>>> hola = "Hola! M'agradaria saludar a: "
>>> hola + "Clara"
"Hola! M'agradaria saludar a: Clara"
>>>
```

Ah ja veig, així que el que fa és **guardar el valor** que posem a la dreta del `=` a la **variable** que definim a l'esquerra del igual.
Així és molt més ràpid utilitzar valors llargs o complicats com `Hola! M'agrad...(massa llarg)`. Programar està bé, però escriure menys està millor.
Anem a provar unes quantes coses més!

### Exercicis de variables

- Puc guardar números a variables?
- Puc veure el contingut d'una variable amb `print`?
- Puc reutilitzar una variable?
- Puc fer operacions entre variables?
- Puc guardar el resultat d'una operació a una variable?
- Una variable pot tenir qualsevol nom?
  - Amb espais?
  - Fins i tot un nom començant amb un número?

```python
>>> tres = 3
>>> print(tres)
3
>>> tres = 4
>>> print(tres)
4
>>> tres = 3
>>> print(tres)
3
>>> trentatres_i_mig = 33.5
>>> print(trentatres_i_mig)
33.5
>>> tres+trentatres_i_mig
36.5
>>> vuit = 4*2
>>> print(vuit)
8
>>> nom1 = "Clara"
>>> tres = "tres"
>>> claratres = nom1+tres
>>> print(claratres)
'Claratres'
>>> nom 2 = "Alba"
  File "<stdin>", line 1
    nom 2 = "Alba"
        ^
SyntaxError: invalid syntax
>>> 2nom = "Alba"
  File "<stdin>", line 1
    2nom = "Alba"
     ^
SyntaxError: invalid syntax
>>>
```

## Interactuant

Tot això està molt bé, però com puc fer programes més complicats però interactuar amb ells.
Per exemple, la taula del 7 és molt complicada, podria fer un programa que multipliqués **el número que jo vulgui** per 7?

A python això ho podem fer amb el comandament `input`. Funciona de manera molt semblant al comandament `print` però mentre `print` ens ensenya el que vulguem per pantalla, el comandament `input`ens permet **guardar el que nosaltres volguem en una variable**.

Aviam com ho podriem fer, obre el document `prova.py` i escrivim això.

```python
num = input("Quin numero vols multiplicar per 7? ")
print(num*7)
```

Si ho executem (amb `python prova.py`) l'ordinador ens preguntara quin número volem multiplicar per 7. Introdueix el número que vulguis i apreta intro!

```bash
Quin numero vols multiplicar per 7? 3
3333333
```

Eeemmm...bé, no està malament però no és ben bé el que esperava. Ens ha pintat el número 3 set vegades, què deu estar passant? Què passaria si en comptes de donar-li un número li demanem una paraula?

```bash
Quin numero vols multiplicar per 7? tres
trestrestrestrestrestrestres
```

Sembla que ho processa tot **com si fos una paraula**, hi ha d'haver alguna manera d'arreglar això.

## Tipus de variables

Les **variables** poden ser de molts tipus. De moment només hem vist **números** i **paraules** perquè són els més comuns.
A Python però hi ha molts tipus de variables (fins i tot en podem crear de nous!) i això és perquè sovint necessitem expresar coses més complexes que números i frases.
Per exemple, si volguessim escriure un programa rencorós, com podria representar si algú em diu una veritat o una mentida?
O guardar la llista de la compra?
O els aniversaris dels meus amics?
Suposo que ho podria fer amb paraules i números, però quina feinada! Hi ha d'haver una manera millor.

Els **5 tipus de variables més comuns** a Python són (i els seus noms dins de Python):

- Paraules/frases (`string`)
- Números (`int` o `float` per a números amb decimals)
- Cert/fals (`bool`, `True/False`)
- Llistes (`list`)
- Diccionaris (`dict`)

# TODO: HOW TO USE/CREATE ALL THESE VAR TYPES
### Excercicis de tipus variables

1. Escriu un programa rencorós que et digui si algú t'ha dit una mentida abans.
2. El mateix programa rencorós però fes que et recordi quantes mentides t'han dit
3. El mateix programa rencorós però que et digui quin dia del més et van mentir

EXEMPLE: Mostrar els tipus d'operacións: = + - * / % ** == != < > <= >= && ||  is  in

