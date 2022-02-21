import numpy as np
X = np.array([[1,4],[2,5],[3,6]])
initial_centroids = np.array([[3, 3], [6, 2], [8, 5]])
y = X[1] - initial_centroids
print(y)