import joblib


def load_model(model_path="model.pkl"):
    return joblib.load(model_path)


def predict(iris_model, x):
    predictions = iris_model.predict(x)
    return predictions
