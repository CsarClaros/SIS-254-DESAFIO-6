import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear un espacio de valores
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Definir los planos de las tres ecuaciones
Z1 = 3 - X - Y
Z2 = (6.00001 - 2*X - 2.00001*Y) / 2
Z3 = (9 - 3*X - 3*Y) / 3.00001

# Crear la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar los tres planos
ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100)
ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100)
ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100)

# Etiquetas de los ejes
ax.set_xlabel('x_1')
ax.set_ylabel('x_2')
ax.set_zlabel('x_3')
plt.title('Gráfico 3D de los planos del sistema 3x3')

plt.show()
