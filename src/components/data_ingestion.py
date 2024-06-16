import pandas as pd
import numpy as np
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from src.logger.my_logging import logging
from src.exception.exception import CustomException

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestionConfig = DataIngestionConfig()

    def init_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            data = pd.read_csv(r"E:\mlops\train.csv")
            logging.info("reading data")
            os.makedirs(os.path.dirname(self.ingestionConfig.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestionConfig.raw_data_path, index=False)
            logging.info("i have saved the raw dataset in artifact folder")
            logging.info("here i have performed train test split")
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("train test split completed")
            train_data.to_csv(self.ingestionConfig.train_data_path, index=False)
            test_data.to_csv(self.ingestionConfig.test_data_path, index=False)
            logging.info("data ingestion part completed")
            return (
                self.ingestionConfig.train_data_path,
                self.ingestionConfig.test_data_path
            )
        except Exception as e:
            logging.error("Error in data ingestion")
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.init_data_ingestion()
