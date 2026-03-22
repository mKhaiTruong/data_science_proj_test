from src.data_science.components.model_evaluation import ModelEvaluation
from src.data_science.config.configuration import ConfigurationManager
from src.data_science import logger

STAGE_NAME = "Model Evaluating stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_eval = ModelEvaluation(config=model_evaluation_config)
        model_eval.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        raise e