from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    download_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    tokenizer_name: str
    dataset_dir: Path
    save_to_dir: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    model_name: str
    dataset_dir: Path
    model_save_to_dir: Path
    tokenizer_save_to_dir: Path