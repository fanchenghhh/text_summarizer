from pathlib import Path

from textSummarizer.constants import CONFIG_FILE, PARAM_FILE
from textSummarizer.entity import DataIngestionConfig
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