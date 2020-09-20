import numpy as np

def test_iris_dataset():
    from sklearn import datasets
    from sklearn.model_selection import train_test_split
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    cmap = ListedColormap(["#FF0000","#00FF00","#0000FF"])

    iris = datasets.load_iris()
    X,y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1234)

    #print(X_train.shape)

    plt.figure()
    plt.scatter(X[:,0], X[:,1], c = y, cmap=cmap, edgecolor='k', s=20)
    plt.show()

    return X_train, X_test, y_train, y_test
#------------------------------------------------------------------
def test_question():
    x1 = [[4,6],[2,4],[4,2],[6,4],[4,4],[6,2]]
    x1 = np.array(x1)
    y1 = [1,1,1,1,2,2]
    y1 = np.array(y1)
    x_test = [[6,6]]
    y_test = [1]
    return x1,x_test,y1,y_test

X_train, X_test, y_train, y_test = test_question()
from knn import KNN

#k = 3 means: Consult nearest 3 neighboues 
classifier = KNN(k=3)

#whole train data is used to fit
classifier.fit(X_train, y_train)
predictions = classifier.predict(np.array(X_test))
print(predictions)

#accuracy
accuracy = np.sum(predictions == y_test) / len(y_test)
print("Accuracy: " + str(accuracy))
