import matplotlib.pyplot as plt
import numpy as np

def myfct (x) : 
    return (x+5-x)

# on genere x valeurs
x = np.linspace(0, 100, 1000)

# on calcule les valeurs de y correspondantes
y = myfct(x)

# on genere la parcelle
plt.plot(x, y)

# on ajoute les infos du graph
plt.xlabel("x")
plt.ylabel("y")
plt.title("Mon graph")

# on affiche le graph
plt.show()
