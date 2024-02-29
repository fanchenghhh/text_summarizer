import logging
import sys
from pathlib import Path

logging_str = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"
log_file = Path("logs/running_logs.log")

log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_file), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("textSummarizer")