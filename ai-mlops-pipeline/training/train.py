import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

mlflow.set_experiment("mlops-iris")

def train():
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    with mlflow.start_run():
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, name="model")

    if accuracy < 0.8:
        raise Exception("Model accuracy below threshold!")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.pkl")

if __name__ == "__main__":
    train()