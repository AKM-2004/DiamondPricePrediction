## yaha per hum bus feature engenerring ki bat kar rahe hai  

from sklearn.impute import SimpleImputer ## HAndling Missing Values
from sklearn.preprocessing import StandardScaler # HAndling Feature Scaling
from sklearn.preprocessing import OrdinalEncoder # Ordinal Encoding
## pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import pandas as pd 
import numpy as np 
import sys,os
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_object
## dara transformation config

@dataclass 
class DataTransformationconfig:
    # yaha per mera pickle file jo ki preprocessor ka hoga uska path hoga

    preprocessor_ob_file = os.path.join('artifacts','preprocessor.pkl')

## Data Ingestion class 

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationconfig()

    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initated')
            #define which coloumn should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut','color','clarity']
            numerical_cols = ['carat','depth','table','x','y','z']
            # Here we are defining the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1', 'SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info('Pipeline Initiated')

            # Now we are going to DO PIPELINE 

            Numerical_Pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler()),
                    
                ]
            )

            Categorical_Pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinal_encodeing',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler())
                ]
            )

            Preprocessor = ColumnTransformer(
                transformers=[
                    ('num_pipeline',Numerical_Pipeline,numerical_cols),
                    ('cat_pipeline',Categorical_Pipeline,categorical_cols)
                ]
            )

            return Preprocessor
        
            logging.info('bhej diya preprocessor')


        except Exception as e:
            logging.info('Miya kuch gafla Hogaya ji transformer mai')


    def initiate_data_transformation(self,train_path,test_path):
        try:
    
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data')
            logging.info(f'train Dataframe head : \n {train_df.head().to_string()}')
            logging.info(f'test Dataframe head : \n {test_df.head().to_string()}')

            logging.info('Obtaning preprocesaing object')
            preprocessing_obj = self.get_data_transformation_object()

            target_coloumn = 'price'
            drop_coloumn = [target_coloumn,'id']
            # mai features ko dependent and independent mai kar raha hu
            input_feature_train_df = train_df.drop(drop_coloumn,axis=1)
            target_feature_train_df = train_df[target_coloumn]
            test_input_feature_df = test_df.drop(drop_coloumn)
            test_target_feature_df = test_df[target_coloumn]
            ## apply transformation 

            input_feature_train_array = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_array = preprocessing_obj.fit_transform(test_input_feature_df)

            target_feature_train_array = preprocessing_obj.transform(target_feature_train_df)
            target_feature_test_array = preprocessing_obj.transform(test_target_feature_df)

            logging.info("Appling preprocessing object on trainig and test")

            train_array = np.concatenate(input_feature_train_array,np.array(target_feature_train_array),axis=1)
            test_array = np.concatenate(input_feature_test_array,np.array(target_feature_test_array),axis=1)

            ## here we saving the preprocesor object
            save_object(file_path=self.data_transformation_config.preprocessor_ob_file,object=preprocessing_obj)
            logging.info("preprocessor pickle is created")

            return (
                train_array,
                test_array,
                self.data_transformation_config.preprocessor_ob_file
            )
        except Exception as e :
            logging.info("Exception occured in the datatransformation")
            raise CustomException(e,sys)















