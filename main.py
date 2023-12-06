from CDC import logger
from CDC.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CDC.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CDC.pipeline.stage_04_evaluation import EvaluationPipeline
from CDC.pipeline.stage_03_training import ModelTrainingPipeline


STAGE_NAME = 'Data Ingestion'
try:
    logger.info('****************************************************************************')
    logger.info(f'>>>>>> Stage [{STAGE_NAME}] started! <<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(
        f'>>>>>> Stage [{STAGE_NAME}] completed! <<<<<<\n\nx=============x\n')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Prepare Base Model'
try:
    logger.info('****************************************************************************')
    logger.info(f'>>>>>> Stage [{STAGE_NAME}] started! <<<<<<')
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(
        f'>>>>>> Stage [{STAGE_NAME}] completed! <<<<<<\n\nx=============x\n')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Training'
try:
    logger.info('****************************************************************************')
    logger.info(f'>>>>>> Stage {STAGE_NAME} started! <<<<<<')
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(
        f'>>>>>> Stage {STAGE_NAME} completed! <<<<<<\n\nx=============x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Evaluation'
try:
    logger.info(f'>>>>>> Stage {STAGE_NAME} started! <<<<<<')
    evaluation = EvaluationPipeline()
    evaluation.main()
    logger.info(
        f'>>>>>> Stage {STAGE_NAME} completed! <<<<<<\n\nx=============x')
except Exception as e:
    logger.exception(e)
    raise e
