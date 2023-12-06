from CDC.config.configuration import ConfigurationManager
from CDC.components.evaluation import Evaluation
from CDC import logger

STAGE_NAME = 'Evaluation'


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>>> Stage {STAGE_NAME} started! <<<<<<')
        evaluation = EvaluationPipeline()
        evaluation.main()
        logger.info(
            f'>>>>>> Stage {STAGE_NAME} completed! <<<<<<\n\nx=============x')
    except Exception as e:
        logger.exception(e)
        raise e
