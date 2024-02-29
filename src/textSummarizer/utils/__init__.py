from pathlib import Path

import yaml
from box import ConfigBox
from box.exceptions import BoxValueError

from textSummarizer.logging import logger


def read_yaml(yaml_file: Path) -> ConfigBox:
    try:
        with open(yaml_file) as f:
            content = yaml.safe_load(f)
            logger.info(f"Reading {yaml_file} ......")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
