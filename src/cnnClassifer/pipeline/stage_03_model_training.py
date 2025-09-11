from cnnClassifer.config.configuration import ConfigurationManager
from cnnClassifer.components.prepare_base_model import Training
from cnnClassifer import logger


STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        logger.info(f"Getting the base model")
        training.get_base_model()
        logger.info(f"Getting the train and valid generator")
        training.train_valid_generator()
        logger.info(f"Training the model")
        training.train()
        

if __name__ == "__main__":
    try:
        logger.info(f"**************************************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e