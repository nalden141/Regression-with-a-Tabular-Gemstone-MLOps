import os
import sys
import pandas as pd
from pathlib import Path


project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from src.logger.my_logging import logging
from src.exception.exception import CustomException

from src.components.data_ingestion import DataIngestion
from src.components.data_transfromation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation


obj=DataIngestion()

train_data_path,test_data_path=obj.init_data_ingestion()

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)


model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)

model_eval_obj = ModelEvaluation()
model_eval_obj.initiate_model_evaluation(train_arr,test_arr)