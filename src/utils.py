import os
import sys
import pickle
import pandas 
import numpy as pd
from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging

def save_object(file_path,object):
    try:
        dir_path = os.pardir.dirname(file_path)

        os.makedirs(file_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dumb(object,file_obj)
    except Exception as e:
        raise CustomException(e,sys)

def evalute_model(xtrain,ytrain,xtest,ytest,models):
    try:
        report = {}
        for keys in models:
            model = models[keys]

            model.fit(xtrain,ytrain)

            y_pred = model.predict(xtest)

            # Now i am going to check the score and we will see which is best 

            model_test_score = r2_score(ytest,y_pred)

            report[keys] = model_test_score

        return report
    
    except Exception as e:
        logging.info ('gafla hogay ji evaluatemodle function mai')
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)






