from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.config import ConfigManager


class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config_manager = ConfigManager()
        data_transformation_config = config_manager.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.transform()