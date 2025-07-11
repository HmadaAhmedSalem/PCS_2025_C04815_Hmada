```python
# Chapitre 3 Exo 1 :
# Initialisation de la liste
L = [1, 2]

# Multiplication de la liste
L3 = 3 * L

# Affichage de L3
print("Contenu de L3 :", L3)  # [1, 2, 1, 2, 1, 2]

# Accès aux éléments de L3
print("L3[0] :", L3[0])       # 1
print("L3[-1] :", L3[-1])     # 2

# Accès à un indice hors limite
try:
    print("L3[10] :", L3[10])
except IndexError as e:
    print("Erreur :", e)      # IndexError: list index out of range

# Création de L4 : carrés des éléments de L3
L4 = [k**2 for k in L3]
print("Contenu de L4 :", L4)  # [1, 4, 1, 4, 1, 4]

# Concaténation de L3 et L4
L5 = L3 + L4
print("Contenu de L5 :", L5)

```

    Contenu de L3 : [1, 2, 1, 2, 1, 2]
    L3[0] : 1
    L3[-1] : 2
    Erreur : list index out of range
    Contenu de L4 : [1, 4, 1, 4, 1, 4]
    Contenu de L5 : [1, 2, 1, 2, 1, 2, 1, 4, 1, 4, 1, 4]
    


```python
# Chapitre 3 Exo2 : 

# Génère 100 valeurs entre 0 et 1, espacées de manière égale
# Utilisation de range(100) pour obtenir les indices de 0 à 99
L = [i / 99 for i in range(100)]

# Affichage des 10 premières valeurs pour vérification
print("Premiers éléments de la liste :", L[:10])
print("Dernier élément :", L[-1])




```





```python

# Chapitre 3 Exo3 : 

#  L[0]
#  Premier élément  0

#  L[-1]
# Dernier élément  0

#  L[:-1]
# Tous les éléments sauf le dernier →
# [0, 1, 2, 1, 0, -1, -2, -1]

# L + L[1:-1] + L
# L[1:-1] = [1, 2, 1, 0, -1, -2, -1]

# Concaténation :
# [0, 1, 2, 1, 0, -1, -2, -1, 0] + [1, 2, 1, 0, -1, -2, -1] + [0, 1, 2, 1, 0, -1, -2, -1, 0]
# Résultat :
# [0, 1, 2, 1, 0, -1, -2, -1, 0, 1, 2, 1, 0, -1, -2, -1, 0, 1, 2, 1, 0, -1, -2, -1, 0]

# L[2:2] = [-3]
# Insertion de -3 à l’indice 2 sans rien remplacer (car début = fin)

# Résultat :
# [0, 1, -3, 2, 1, 0, -1, -2, -1, 0]

# L[3:4] = []
# Supprime l’élément à l’indice 3 → ici 2 est à l’indice 3 après l'insertion précédente

# Nouvelle liste :
# [0, 1, -3, 1, 0, -1, -2, -1, 0]

# L[2:5] = [-5]
# Remplace les éléments d’indice 2 à 4 inclus (soit -3, 1, 0) par [-5]

# Nouvelle liste :
# [0, 1, -5, -1, -2, -1, 0]
```


```python

#Chapitre 3 Exo 4 : 

# L = [n - m/2 for n in range(m)]

# - `range(m)` génère : `0, 1, ..., m-1`
# - Chaque élément devient : `n - m/2`
# - Donc :  
#   L = [0 - m/2, 1 - m/2, ..., (m-1) - m/2]

# #### 2. **Éléments extrêmes**

# - L[0] = -m/2
# - L[-1] = (m - 1) - m/2

# Calcul de `ans`: 



# ans = 1 + L[0] + L[-1] = 1 - m/2 + (m - 1) - m/2)


# ans = 1 - m/2 + m - 1 - m/2 = 0 + m - m = 0



```


```python

# Chapitre 3 Exo 5:

import numpy as np
import matplotlib.pyplot as plt

# Paramètres
dt = 0.1
T = 10
N = int(T / dt)

# Temps discret
td = [i * dt for i in range(N + 1)]

# Initialisation de u
u = [1, 1, 1]  # u0 = u1 = u2 = 1 (donné dans l'énoncé)

# Formule de récurrence multistep (hypothèse)
for n in range(2, N):
    next_u = 2 * u[n] - u[n - 1] - dt**2 * u[n - 2]
    u.append(next_u)

# Solution exacte (supposée être u(t) = cos(t))
u_exact = [np.cos(t) for t in td]

# Différence
diff = [u[i] - u_exact[i] for i in range(len(td))]

# Tracé 1 : u vs td
plt.figure(figsize=(10, 4))
plt.plot(td, u, label='u (approximation)', color='blue')
plt.plot(td, u_exact, label='u_exact = cos(t)', linestyle='--', color='orange')
plt.xlabel("Temps (t)")
plt.ylabel("u(t)")
plt.title("Comparaison entre u et la solution exacte")
plt.legend()
plt.grid(True)
plt.show()

# Tracé 2 : Différence u - u_exact
plt.figure(figsize=(10, 4))
plt.plot(td, diff, label='Erreur (u - u_exact)', color='red')
plt.xlabel("Temps (t)")
plt.ylabel("Erreur")
plt.title("Erreur entre l'approximation numérique et la solution exacte")
plt.legend()
plt.grid(True)
plt.show()
```

```python
#Chapitre 3 Exo 6 :

def symmetric_difference_manual(A, B):
    # A \ B : éléments dans A mais pas dans B
    diff_A = A - B
    # B \ A : éléments dans B mais pas dans A
    diff_B = B - A
    # Union des deux
    return diff_A | diff_B

# Exemple
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result_manual = symmetric_difference_manual(A, B)
result = A.symmetric_difference(B)
print("Différence symétrique (manuel) :", result_manual)
print("Différence symétrique (builtin) :", result)


```



```python
#Chapitre 3 Exo 7:

# Définition de l'ensemble vide
empty_set = set()

# Quelques ensembles pour tester
A = {1, 2, 3}
B = set()
C = {'a', 'b', 'c'}

# Vérifications
print("∅ ⊆ A ?", empty_set.issubset(A))  # True
print("∅ ⊆ B ?", empty_set.issubset(B))  # True
print("∅ ⊆ C ?", empty_set.issubset(C))  # True
```
    
```python
# Chapitre 3 Exo 8 : 

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Avant intersection_update:")
print("A =", A)
print("B =", B)

# intersection → retourne un nouvel ensemble
C = A.intersection(B)
print("\nRésultat de A.intersection(B) :", C)
print("A (inchangé) :", A)

# intersection_update → modifie A
A.intersection_update(B)
print("\nA après A.intersection_update(B) :", A)
```
