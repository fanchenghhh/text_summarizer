
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.config import ConfigManager


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config_manager = ConfigManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.unzip_data()