import numpy as np
from collections import Counter

def eucildean_distance(x1, x2):
    return np.sqrt(np.sum((x1-x2)**2))

class KNN:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        """KNN not requires a training step, hence we simply store x as X_train, y as y_train"""
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """X is a list"""
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x):
        #compute distances
        distances = [eucildean_distance(x, coordinate) for coordinate in self.X_train]

        #get nearest k samples, labels
        indexed_distances = list(enumerate(distances))
        k_nearest_distances = sorted(indexed_distances, key = lambda x: x[1])[:self.k]
        k_nearest_labels = [self.y_train[i[0]] for i in k_nearest_distances]

        #vote
        most_common_label = Counter(k_nearest_labels).most_common(1)
        #most_common method of Counter returns top k most common apperances as [(element1, count1), (element2, count2), ....]
        return most_common_label[0][0]

"""lis = ["banana","apple","orange","pomegranate"]
color = ["yell","red","orange","red"]
lis_new = list(enumerate(lis))
lis_new_n = sorted(lis_new, key = lambda x:x[1])[:3]
lis_new_n_labels = [color[i[0]] for i in lis_new_n]
print(lis_new_n_labels)"""