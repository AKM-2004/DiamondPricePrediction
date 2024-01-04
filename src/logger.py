import logging
import os
from datetime import datatime 

log_fi = f"{datatime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # this is our file path of our log
file_path = os.path.join(os.getcwd(),"logs",log_fi) # here we are making the folder path for that 
os.makedirs(file_path,mode=777,exist_ok=True) # here we are making the folder for my path

log_fi_path = os.path.join(file_path,log_fi)

logging.basicConfig(
    filename= log_fi_path,
    format="[%(asctime)s] %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)
