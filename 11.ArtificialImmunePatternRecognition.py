import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

class AISClassifier:
    def __init__(self,n_antibodies=10):
        self.n_antibodies = n_antibodies

    def fit(self,X,Y):
        self.antibodies = np.random.rand(self.n_antibodies,X.shape[1])
        self.labels = np.random.choice(np.unique(Y),size=self.n_antibodies)
    
    def predict(self,X):
        return [self.labels[np.argmin(np.linalg.norm(self.antibodies-x,axis=1))] for x in X]

model = AISClassifier(n_antibodies=10)
model.fit(X_train,Y_train)
y_pred = model.predict(X_test)

print('Accuracy:',accuracy_score(Y_test,y_pred))