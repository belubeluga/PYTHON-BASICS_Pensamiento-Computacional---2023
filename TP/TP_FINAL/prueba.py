import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pygame

# Now you can use the `ax` object to create your 3D plot.

# For example, let's create a simple 3D scatter plot.
'''x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

ax.scatter(x, y, z)'''

#cubo
cubo = np.ones((3,3,3), dtype = 'bool')
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.voxels(cubo,facecolor = '#E02050',edgecolor = "k")

# Show the plot
plt.show()