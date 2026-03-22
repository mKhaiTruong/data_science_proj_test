import os, joblib
from pathlib import Path


class PredictPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
    
    def predict(self, data):
        return self.model.predict(data)