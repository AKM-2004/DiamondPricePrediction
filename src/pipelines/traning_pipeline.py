from sklearn.pipeline import Pipeline
import pandas as pd 
import os 
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
import pandas as pd
from src.components.model_tranier import ModelTranier
if __name__ == "__main__":
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)

    data_transformation =DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_path=train_data_path,test_path=test_data_path)
    model_trainer = ModelTranier()

    model_trainer.initate_model_traning(train_arr,test_arr)



