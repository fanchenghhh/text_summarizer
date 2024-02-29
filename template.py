from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

project_name = "textSummarizer"

file_list = [
    "requirements.txt",
    "setup.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    "main.py",
    "notebooks/trial.ipynb",
    f"configs/config.yaml",
    f"params/param.yaml",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/models/__init__.py",
    "app.py",
]

for file in file_list:
    file_path = Path(file)
    folder = file_path.parent
    folder.mkdir(parents=True, exist_ok=True)
    if not file_path.exists():
        with open(file_path, "w", encoding="utf-8") as f:
            logging.info(f"Create empty file {file_path}")
    else:
        logging.info(f"File {file_path} exists already")


    