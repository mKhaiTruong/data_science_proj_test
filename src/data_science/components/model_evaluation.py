import os, pandas as pd, numpy as np
import joblib
import mlflow, mlflow.sklearn
from pathlib import Path
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from src.data_science.config.configuration import ModelEvaluationConfig
from src.data_science.utils.common import save_json 

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae  = mean_absolute_error(actual, pred)
        r2   = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            
            predicted_qualities = model.predict(test_x)

            (self.rmse, self.mae, self.r2_score) = self.eval_metrics(test_y, predicted_qualities)
            score = {"rmse": self.rmse, "mae": self.mae, "r2_score": self.r2_score}
            save_json(path=Path(self.config.metric_file_name), data=score)
            
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", self.rmse)
            mlflow.log_metric("mae", self.mae)
            mlflow.log_metric("r2_score", self.r2_score)

            
            if tracking_url_type_store != 'file':
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetWineModel")
            else:
                mlflow.sklearn.log_model(model, "model")