from src.cnnClassifer import logger
from src.cnnClassifer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipelne
from src.cnnClassifer.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


logger.info("Starting the Kidney Disease Classification Process")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipelne()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e