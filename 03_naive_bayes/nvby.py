import numpy as np
from sklearn.naive_bayes import GaussianNB
X = np.array([
              [0, 0, 0, 0],
              [0, 0, 0, 1],
              [1, 0, 0, 0],
              [2, 1, 0, 0],
              [2, 2, 1, 0],
              [2, 2, 1, 1],
              [1, 2, 1, 1],
              [0, 1, 0, 0],
              [0, 2, 1, 0],
              [2, 1, 1, 0],
              [0, 1, 1, 1],
              [1, 1, 0, 1],
              [1, 0, 1, 0],
              [2, 1, 0, 1]
])# Label
Y = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0])
model = GaussianNB()
model.fit(X, Y)
print(model.predict([[0, 0, 0, 0]]))