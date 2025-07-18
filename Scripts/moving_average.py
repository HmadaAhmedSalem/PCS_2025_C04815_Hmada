# moving_average.py

import numpy as np

def moving_averagef(u, n):
    """
    Calcule la moyenne glissante de taille n sur le tableau u.
    
    Paramètres :
    - u : tableau 1D de données
    - n : entier, taille de la fenêtre
    
    Retour :
    - tableau numpy contenant les moyennes glissantes
    """
    if n <= 0:
        raise ValueError("n doit être strictement positif")
    if len(u) < n:
        raise ValueError("Le tableau u est trop court pour n =", n)

    kernel = np.ones(n) / n
    return np.convolve(u, kernel, mode='valid')
