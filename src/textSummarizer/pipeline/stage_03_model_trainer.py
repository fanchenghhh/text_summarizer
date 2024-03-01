
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.config import ConfigManager


class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config_manager = ConfigManager()
        model_trainer_config = config_manager.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()