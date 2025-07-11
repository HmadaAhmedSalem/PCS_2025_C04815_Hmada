```python
# Chapitre 2 Exo 1:

def f(x):
    return x**2 - 0.25*x + 5

x = 2.3
resultat = f(x)

if resultat == 0:
    print(f"x = {x} est une racine de la fonction.")
else:
    print(f"x = {x} n'est pas une racine de la fonction (f(x) = {resultat}).")
```
    

```python
# Chapitre 2 Exo2 :

import cmath  # Bibliothèque pour les nombres complexes

# declaration et affectation des valeurs
n = 3
x = cmath.pi / 4  # x en radians

# Deuxième partie : (cos x + i sin x)^n
z = cmath.cos(x) + 1j * cmath.sin(x)
deuxieme_partie = z ** n

# Première partie : cos(n x) + i sin(n x)
premiere_partie = cmath.cos(n * x) + 1j * cmath.sin(n * x)

# Affichage des résultats
print("Première partie : cos(n x) + i sin(n x) =", premiere_partie)
print("Deuxième partie : (cos(x) + i sin(x))^n =", deuxieme_partie)

# Vérification
if premiere_partie == deuxieme_partie:
    print("La formule de De Moivre est vérifiée.")
else:
    print("La formule de De Moivre n'est pas vérifiée.")


    
```


```python
# Chapitre 2 Exo 3:

import cmath

# declaration et affectaion de variable
x = cmath.pi / 3  # par exemple x = π/3

# Première partie : e^(ix)
premiere_partie = cmath.exp(1j * x)

# Deuxième partie : cos(x) + i*sin(x)
deuxieme_partie = cmath.cos(x) + 1j * cmath.sin(x)

# Affichage des résultats
print("Première partie : e^(ix) =", premiere_partie)
print("Deuxième partie : cos(x) + i*sin(x) =", deuxieme_partie)

# Vérification avec tolérance
tolerance = 1e-10
if abs(premiere_partie - deuxieme_partie) < tolerance:
    print("La formule d'Euler est vérifiée.")
else:
    print("La formule d'Euler n'est pas vérifiée.")
```
    


```python
#Chapitre 2 Exo 4:
u = 1.0  # valeur initiale (flottant)
uold = 10.0  # valeur de comparaison arbitraire au départ

for iteration in range(2000):
    if not abs(u - uold) > 1.e-8:
        print('Convergence')
        break  # la suite est considérée comme convergente
    uold = u
    u = 2 * u
else:
    print('No convergence')  # si la boucle se termine sans break



    # Question 1 : le code affiche 'convergence' mais pas d’une vraie convergence mathématique !.
    # Question 2 : Apparemment, le changement ne donne pas le même résultat !
    # Question 3 : Si je remplace u=1.0 par u= 1 (changement e type implicitement) le programe affiche No convergence.

# Question 4 : 
# La suite est divergente par définition, mais lorsqu’on exécute le programme avec u = 1.0 (un float), le code affiche "Convergence", alors qu’avec u = 1 (un int), il affiche "No convergence".

# Ce phénomène s'explique par une fausse convergence numérique, causée par :

# l’utilisation des nombres flottants (float), qui ont une précision limitée (environ 16 chiffres significatifs en Python),

# la saturation des floats et la perte de précision qui rend u et uold identiques aux yeux du programme, même s’ils devraient être différents.

```    


```python
# Chapitre 2 Exo 5 :

def implication(A, B):
    return not A or B
```


```python
# Chapitre 2 Exo 6 :
def half_adder(p, q):
    somme = p ^ q       # XOR pour la somme
    retenue = p & q     # AND pour la retenue
    return (somme, retenue)
    
def full_adder(p, q, cin):
    # Première addition : p + q
    s1, c1 = half_adder(p, q)
    # Deuxième addition : (p + q) + cin
    somme, c2 = half_adder(s1, cin)
    # Retenue finale = c1 OR c2
    retenue = c1 | c2
    return (somme, retenue)
```
