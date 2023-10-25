import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Función para dibujar un cubo
def draw_cube(ax, center, size):
    x, y, z = center
    dx, dy, dz = size
    # Coordenadas de los vértices del cubo
    vertices = [
        [x - dx, y - dy, z - dz],
        [x - dx, y - dy, z + dz],
        [x - dx, y + dy, z - dz],
        [x - dx, y + dy, z + dz],
        [x + dx, y - dy, z - dz],
        [x + dx, y - dy, z + dz],
        [x + dx, y + dy, z - dz],
        [x + dx, y + dy, z + dz]
    ]
    # Aristas del cubo
    edges = [
        [vertices[0], vertices[1], vertices[3], vertices[2], vertices[0]],
        [vertices[4], vertices[5], vertices[7], vertices[6], vertices[4]],
        [vertices[0], vertices[4]],
        [vertices[1], vertices[5]],
        [vertices[2], vertices[6]],
        [vertices[3], vertices[7]]
    ]

    for edge in edges:
        x, y, z = zip(*edge)
        ax.plot(x, y, z, color='b')

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar cubos
cubos = [
    ((7, 0, 3), (1, 0.3, 0.3)),
    ((5, 5,5), (0.1, 0.3,0.6)),
    ((4, 0, 0), (0.2, 0.2, 0.2)),
    ((7, 5, 3), (1, 0.3, 0.3)),
    ((4, 4,5), (0.1, 0.3,0.6)),
    ((11, 11, 11), (0.2, 0.2, 0.2)),
]

for centro, tamaño in cubos:
    draw_cube(ax, centro, tamaño)

# Configuración de la vista
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Espacio 3D con Cubos')

# Mostrar la visualización
plt.show()
