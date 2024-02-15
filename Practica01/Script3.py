import matplotlib.pyplot as plt
import numpy as np

#graficando la rosa polar de cuatro petalos
#theta indica el angulo polar
theta = np.linspace(0, 2*np.pi, 1000)
#k indica la cantidad de petalos a graficar
k = 4
#r indica la distancia del origen al punto en la curva
r = np.sin(k*theta)
plt.polar(theta, r, "r")
plt.show()