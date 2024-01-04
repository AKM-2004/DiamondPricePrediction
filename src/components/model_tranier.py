import pandas as pd 
import numpy as np 
import os 
import sys
from src.components.data_transformation import DataTransformation
from src.exception import CustomException
from src.logger import logging
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from dataclasses import dataclass
from src.utils import save_object,evalute_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path  = os.path.join('artifacts','model.pkl')

class ModelTranier:
    def __init__(self):
        self.Model_config = ModelTrainerConfig()
    
    def initate_model_traning(self,train_arr,test_arr):
        try:
            x_train,y_train,x_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            model = {
                "LinerRegression":LinearRegression(),
                "Ridge":Ridge(),
                "Lasso":Lasso(),
                "ElasticNet":ElasticNet()
            }

            # jo jo models try karna hai vo keyvalue mai likh do

            model_report:dict = evalute_model(x_train,y_train,x_test,y_test)
            print(model_report)
            print("\n============================================================")
            logging.info(f'Model report :{model_report}')

            # to get best model score from dictionary

            best_model_score = max(sorted(model_report).values())

            name_of_best_model = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            print(f"mere bahi yo best model humhara hai {name_of_best_model}")
            logging.info(f" our best model is {name_of_best_model}")

            best_model = model[name_of_best_model]

            save_object(
                file_path = self.Model_config.trained_model_file_path,
                object=best_model

            )
        except Exception as e:
            logging.info("model failure hogaya meri jan")
            raise CustomException(e,sys)



    
    
    

    
    
    






