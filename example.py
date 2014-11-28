import numpy as np
import matplotlib.pyplot as plt
from cubepk import get_coord

points = 20
x = np.random.randn(points)
y = np.random.randn(points)
colors = get_coord(points)
plt.figure(figsize=(16, 12))
plt.scatter(x, y, c=colors, s=100)
plt.show()
