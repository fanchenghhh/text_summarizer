import os

from textSummarizer.pipeline.stage_03_model_trainer import \
    ModelTrainerTrainingPipeline

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import \
    DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_transformation import \
    DataTransformationTrainingPipeline

if __name__ == "__main__":
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


    STAGE_NAME = "Data Transformation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e



    STAGE_NAME = "Model Trainer stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_transformation = ModelTrainerTrainingPipeline()
        data_transformation.train()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e