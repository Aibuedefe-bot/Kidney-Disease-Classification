from src.cnnClassifer import logger
from src.cnnClassifer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipelne

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