from src.data_science import logger
from src.data_science.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.data_science.pipeline.data_validation_pipeline import DataValidationPipeline
from src.data_science.pipeline.data_transformation_pipeline import DataTransformationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        raise e

STAGE_NAME = "Data Validation stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        raise e

STAGE_NAME = "Data Transformation stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        raise e