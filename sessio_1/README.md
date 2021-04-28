# Introducció a la programació en Python

Els llenguatges de programació ens permeten **comunicar-nos amb els ordinadors** i demanar-los que ens facin qualsevol seguit de tasques.
`Python` es un **llenguatge de programació modern** (dels anys 90) i molt extès a totes les indústries ja que és molt **versàtil** i **senzill**.
Els dissenyadors de `Python` el defineixen com "**el 2n millor llenguatge per a fer qualsevol tasca**", `Python` no és el millor llenguatge per a cap tasca en concret, però permet fer qualsevol tasca que puguis imaginar molt fàcilment.

## On puc trobar Python

`Python` és gratuït i es pot descarregar de la seva web oficial: [https://www.python.org](https://www.python.org)

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

### Exercicis

- Es poden sumar dues paraules?
- Es poden sumar un número i una paraula?
- Es poden multiplicar números? (pista: l'operador de multiplicar és `*`)
- Es poden multiplicar paraules?

```python
>>> "hola" + "mon"
'holamon'
>>> "tres es " + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 3*7
21
>>> "onze"*3
'onzeonzeonze'
>>> 
```

Ja veus que `Python` és bastant intuïtiu, i també és bastant evident quan alguna cosa no li ha agradat.

## Organitzant el codi

Treballar amb la terminal de `Python` pot ser força útil, però els ordinadors "funcionen sols", no hi ha una persona enganxada a l'ordinador escrivint-hi operacions. Com es fa això?

Les operacions i tasques es deixen escrites en **fitxers de text** per a que l'**ordinador els llegeixi i els processi**.

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

EXEMPLE: Mostrar els tipus d'operacións: = + - * / % ** == != < > <= >= && ||  is  in

3 - Què és una variable
EXEMPLE: crear una variable i fer un print del valor
EXEMPLE: canviar el valor de la variable i fer el print
EXEMPLE: crear dos variables, fer operacións entre elles i guardar-ho en una tercera i fer print

input command per a jugar

4 - Tipus de variables: numero, bool, string, list, map
EXEMPLE: crear un bool
EXEMPLE: crear un int
EXEMPLE: crear una string
