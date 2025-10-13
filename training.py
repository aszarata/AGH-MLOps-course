import os
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
import joblib


def load_data():
    iris = load_iris()
    X, y = iris.data, iris.target
    return X, y


def train_model():
    X, y = load_data()
    iris_model = MLPClassifier(max_iter=1000)
    iris_model.fit(X, y)
    return iris_model


def save_model(iris_model, model_path=os.path.join("models", "iris.joblib")):
    train_model()
    joblib.dump(iris_model, model_path)


if __name__ == "__main__":
    model = train_model()
    save_model(iris_model=model)
