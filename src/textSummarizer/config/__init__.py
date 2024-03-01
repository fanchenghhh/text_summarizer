from pathlib import Path

from textSummarizer.constants import CONFIG_FILE, PARAM_FILE
from textSummarizer.entity import (DataIngestionConfig,
                                   DataTransformationConfig,
                                   ModelTrainerConfig)
from textSummarizer.utils import read_yaml


class ConfigManager:
    def __init__(self, config_file: Path = CONFIG_FILE, param_file: Path = PARAM_FILE):
        self.config = read_yaml(config_file)
        self.param = read_yaml(param_file)

        Path(self.config.artifact_root).mkdir(parents=True, exist_ok=True)
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        return DataIngestionConfig(
            download_url =config.download_url, 
            local_data_file =Path(config.local_data_file), 
            unzip_dir =Path(config.unzip_dir), 
            )
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        return DataTransformationConfig(
            dataset_dir=Path(config.dataset_dir),
            tokenizer_name=config.tokenizer_name,
            save_to_dir=Path(config.save_to_dir)
            )
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer

        return ModelTrainerConfig(
            model_name=config.model_name,
            dataset_dir=config.dataset_dir,
            model_save_to_dir=config.model_save_to_dir,
            tokenizer_save_to_dir=config.tokenizer_save_to_dir
            )
    
    def get_param(self):
        return self.param