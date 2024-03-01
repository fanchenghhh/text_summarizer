from datasets import load_from_disk
from transformers import AutoTokenizer

from textSummarizer.entity import DataTransformationConfig
from textSummarizer.logging import logger


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def convert_example_to_feature(self, examples):
        dialogue_encoding = self.tokenizer(examples["dialogue"], max_length=1024, truncation=True)
        with self.tokenizer.as_target_tokenizer():
            summary_encoding = self.tokenizer(examples["summary"], max_length=128, truncation=True)
        
        return {
            "input_ids": dialogue_encoding["input_ids"],
            "labels": summary_encoding["input_ids"],
            "attention_mask": dialogue_encoding["attention_mask"]
        }
        

    def transform(self):
        logger.info(f"Tranforming samples to features...")
        dataset = load_from_disk(self.config.dataset_dir)
        feature = dataset.map(self.convert_example_to_feature, batched=True)
        self.config.save_to_dir.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Saving features to {self.config.save_to_dir}...")
        feature.save_to_disk(self.config.save_to_dir)
        