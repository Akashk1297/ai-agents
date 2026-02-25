```This project will include:
Model training
MLflow model versioning
FastAPI inference API
Dockerization
CI pipeline (GitHub Actions)
Kubernetes deployment
Auto validation before deploy```

## Project Structure
```
mlops-pipeline/
│
├── app/
│   ├── main.py
│   ├── model_loader.py
│   └── schema.py
|   └── _init_.py
│
├── training/
│   ├── train.py
│   └── preprocess.py
│
├── tests/
│   └── test_api.py
│
├── Dockerfile
├── requirements.txt
├── k8s-deployment.yaml
├── .github/workflows/ci.yml
└── README.md
```

## Activate Your Virtual Environment (Recommended)

If you are inside your project folder:
```
python -m venv venv
```

Activate it:
```
source venv/Scripts/activate
```

## Install Dependencies
Run:
```
pip install -r requirements.txt
touch app/__init__.py
```

## Run Training Again
```
$ python training/train.py
2026/02/24 16:48:49 INFO mlflow.store.db.utils: Creating initial MLflow database tables...
2026/02/24 16:48:49 INFO mlflow.store.db.utils: Updating database tables
2026/02/24 16:48:50 INFO mlflow.tracking.fluent: Experiment with name 'mlops-iris' does not exist. Creating a new experiment.
2026/02/24 16:48:49 INFO mlflow.store.db.utils: Creating initial MLflow database tables...
2026/02/24 16:48:49 INFO mlflow.store.db.utils: Updating database tables
2026/02/24 16:48:50 INFO mlflow.tracking.fluent: Experiment with name 'mlops-iris' does not exist. Creating a new experiment.
2026/02/24 16:48:49 INFO mlflow.store.db.utils: Updating database tables
2026/02/24 16:48:50 INFO mlflow.tracking.fluent: Experiment with name 'mlops-iris' does not exist. Creating a new experiment.
2026/02/24 16:48:50 INFO mlflow.tracking.fluent: Experiment with name 'mlops-iris' does not exist. Creating a new experiment.
2026/02/24 16:48:51 WARNING mlflow.models.model: `artifact_path` is deprecated. Please use `name` instead.
2026/02/24 16:48:51 WARNING mlflow.sklearn: Saving scikit-learn models in the pickle or cloudpickle format requires exercising caution becau2026/02/24 16:48:51 WARNING mlflow.models.model: `artifact_path` is deprecated. Please use `name` instead.
2026/02/24 16:48:51 WARNING mlflow.sklearn: Saving scikit-learn models in the pickle or cloudpickle format requires exercising caution becau2026/02/24 16:48:51 WARNING mlflow.sklearn: Saving scikit-learn models in the pickle or cloudpickle format requires exercising caution because these formats rely on Python's object serialization mechanism, which can execute arbitrary code during deserialization. The recommended safe alternative is the 'skops' format. For more information, see: https://scikit-learn.org/stable/model_persistence.html
(venv)
```

## 🔥 How To Run Locally

### Train Model
```
python training/train.py
```


## 🚀 Next Step

### Now test the API:

#### Reload
```
$ python -m uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['E:\\Devops LLM\\ai-agents\\ai-mlops-pipeline']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [17964] using StatReload
INFO:     Started server process [13480]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:60495 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:60495 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:58998 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:58998 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:50134 - "POST /predict HTTP/1.1" 200 OK
```

Then open browser and visit:
```
http://127.0.0.1:8000/docs
```

Try POST request:
```
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```