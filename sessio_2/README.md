# Sessió 2: Començant a programar

A la primera sessió hem après les bases per a començar a programar, les eines: `python` i fitxers `*.py`, i les peces bàsiques: `variables`, rebre informació de l'usuari, i mostrar valors per pantalla.

A la segona sessió aprendrem les primeres eines per a poder fer programes una mica més interessants.

## Condicionals

Sovint un programa ha de fer **diferents coses segons la situació**. Per exemple, a l'estiu l'aire acondicionat s'activa si fa massa calor, o al metro les portes ens deixen passar només si el nostre bitllet és vàlid.

Aquestes màquines poden fer això gràcies als **condicionals**, que sovint expresem en la forma:

- Si fa calor: engega l'aire acondicionat
- Si no: apaga'l

O:

- Si el bitllet és vàlid: deixa passar al passatger
- Si no: demana que compri un bitllet vàlid

A `python` això ho expresem amb les paraules `if` (si en anglès) i `else` (si no en anglès). Per exemple:

```python
if temperatura > 26:
    aire_acondicionat = True
    print("Engegant l'aire acondicionat")
else:
    aire_acondicionat = False
    print("Aturant l'aire acondicionat, hem d'estalviar energia!")
```

o

```python
if bittlet_valid:
    porta_oberta = True
    print("Porta oberta, bon viatge!")
else:
    porta_oberta = False
    print("Per favor, compra un bitllet nou a la maquina")
```

És bastant senzill de fet! Darrera del `if` posem la condició que volem que es compleixi (exemple: `temperatura > 26`) i a continuació `:`. Després a les següents línies (i `indentat`) posem tot el que volem que passi en aquesta condició.
A continuació, **opcionalment**, podem posar què volem que passi en cas contrari amb `else` i els `:`.

### Petit apunt sobre `indentació` i `:`

A `python` el codi l'estructurem sovint en diferents **blocs** que indentem i separem amb els 2 punts (`:`).
Sovint si `python` es queixa és per què us falta algun d'aquests 2 elements, i us donarà indicacions d'on falta i què falta.

Exemples:

```python
# aqui falten els :
>>> temp = 25
>>> if temp>26
  File "<stdin>", line 1
    if temp>26
             ^
SyntaxError: invalid syntax
```

```python
# aqui la linia print no esta ben indentada
>>> temp = 25
>>> if temp>26:
... print("hola")
  File "<stdin>", line 2
    print("hola")
        ^
IndentationError: expected an indented block
```

### Excercicis de condicionals

1. Prova que `else` és realment opcional
2. Quin és el "valor" de `temp>25`? (pista: prova de fer `print`)
   1. Ara les variables condicionals tenen més sentit! `True/False`
3. Fes una petita calculadora que et demani dos números i un símbol per a fer una operació (símbols `+` `-` `*` `/`)

## Operadors lògics

Hem vist que per poder fer servir els **condicionals** (`if/else`) necessitem **una condició**.

Les condicions sovint són coses com:

- `True`, `False`
  - cert/fals
  - totes les condicions acaben sent certes o falses
- `==`, `!=`
  - igual, diferent
- `>`, `>=`, `<`, `<=`
  - més gran, més gran o igual, més petit, més petit o igual

Tot i que a vegades volem **expressar més d'una condició o combinació de condicions**.

Com expresem que volem que una cosa sigui certa **i** una altra sigui falsa?
O que una condició **o** una altra siguin certes?
A `python` expressem això amb les paraules angleses `and` (**i**) i `or` (**o**).

Tornant a l'exemple de l'aire acondicionat, l'aire potser només funciona si hi ha electricitat a la casa.

```python
if temperatura > 26 and tenim_electricitat:
    aire_acondicionat = True
    print("Engegant l'aire acondicionat")
else:
    aire_acondicionat = False
    print("Aturant l'aire acondicionat, hem d'estalviar energia (o potser no en tenim)!")
```

O potser també volem engegar l'aire acondicionat si ho demanem manualment:

```python
if temperatura > 26 or manual:
    aire_acondicionat = True
    print("Engegant l'aire acondicionat")
else:
    aire_acondicionat = False
    print("Aturant l'aire acondicionat, hem d'estalviar energia!")
```

O fins i tot una combinació de les dues!

```python
if tenim_electricitat and (temperatura > 26 or manual):
    aire_acondicionat = True
    print("Engegant l'aire acondicionat")
else:
    aire_acondicionat = False
    print("Aturant l'aire acondicionat, hem d'estalviar energia!")
```

Els parèntesis serveixen per assegurar que les condicions es comproven en l'ordre adequat, no és el mateix:

1. `tenim_electricitat and (temperatura > 26 or manual)`
2. `(tenim_electricitat and temperatura > 26) or manual`

En la segona condició l'aire acondicionat s'engegarà si ho demanes manualment encara que no hi hagi electricitat! I això em sembla que no és possible 🤔.

## TODO:

3 - bucles d'iteració: for, while, range
    Explicar com repetir una acció sense haver de copiar 234976247 vegades la mateixa línia
    Si sabem quantes vegades ho volem, amb un for.
    EXEMPLE: Sabem que si sumem 10 vegades 10 donarà 100. Aleshores anem sumant en una variable i en traguem el resultat
    Si no sabem quantes vegades però sabem quan parar, bucle while
    EXEMPLE: Cas invers al següent, while(x!=100) anem sumant i registrem el número de loops que haurà de ser 10

Projectet per a utilitzar variables i flow control
