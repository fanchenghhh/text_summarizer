import os
import urllib.request as request
import zipfile

from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        self.config.local_data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.config.local_data_file.exists():
            filename, headers = request.urlretrieve(
                url=self.config.download_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded!")
        else:
            logger.info(f"{self.config.local_data_file} exists already!")
        

    def unzip_data(self):
        self.config.unzip_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
            logger.info(f"unzip {self.config.unzip_dir}")