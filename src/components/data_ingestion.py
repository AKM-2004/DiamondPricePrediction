import os 
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## initialize data ingestion configure

@dataclass # ye 
class Dataingestionconfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')
## create a data ingesion class
class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = Dataingestionconfig()

    def initiate_data_ingestion(self):
        # Iss function ko ab hum yaha sab karegai train test split and usko csv mai convert karna
        logging.info('Data ingestion start hogaya hai')

        try:
            df = pd.read_csv(os.join.path('notebook/data','gemstone.csv'))
            logging.info('Bhai pandas nai read karliyaa')

            os.mkdir(os.path.join(self.ingestion_config.raw_data_path),exst_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False) # yaha pura ki pura save ho raha hai humere artifacts mai taki mai kabhi bhi data ek secondary jagaha per rakh saku

            logging.info("Trian test split")

            train_split,test_split = train_test_split(df,test_size=0.30,random_state=32)
            train_split.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_split.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of data is complitated")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )






        except Exception as e:
            logging.info('Error occured in data config')