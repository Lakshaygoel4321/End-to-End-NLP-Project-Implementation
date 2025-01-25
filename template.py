import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctiime)s]: %(message)s:')

PROJECT_NAME = "hate"

list_of_file = [

    f"{PROJECT_NAME}/components/__init__.py",
    f"{PROJECT_NAME}/components/data_ingestion.py",
    f"{PROJECT_NAME}/components/data_transformation.ppy",
    f"{PROJECT_NAME}/components/model_evaluation.py",
    f"{PROJECT_NAME}/components/model_trainer.py",
    f"{PROJECT_NAME}/components/model_pusher.py",
    
    f"{PROJECT_NAME}/configuration/__init__.py",
    f"{PROJECT_NAME}/configuration/gcloud_syncer.py",

    f"{PROJECT_NAME}/constant/__init__.py",

    f"{PROJECT_NAME}/entity/__init__.py",
    f"{PROJECT_NAME}/entity/config_entity.py",
    f"{PROJECT_NAME}/entity/artifcat_entity.py",
    
    f"{PROJECT_NAME}/exception/__init__.py",

    f"{PROJECT_NAME}/logger/__init__.py",

    f"{PROJECT_NAME}/pipeline/__init__.py",
    f"{PROJECT_NAME}/pipeline/prediction_pipeline.py",
    f"{PROJECT_NAME}/pipeline/train_pipeline.py",

    #f"{PROJECT_NAME}/utils/__init__.py",
    #f"{PROJECT_NAME}/utils/main_utils.py",

    f"{PROJECT_NAME}/ml/__init__.py",
    #f"{PROJECT_NAME}/ml/feature.py",
    f"{PROJECT_NAME}/ml/models.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"

]

for filepath in list_of_file:
    filepath = Path(filepath)

    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory;{filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")

