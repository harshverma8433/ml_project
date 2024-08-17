import os
# os module is for interact with the the operating system
import sys 
# sys module is for interact with the accessing system-specific parameters
from src.exception import CustomException
# a custom exception class imported from src.exception used to handle errors
from src.logger import logging
# during the exception a src.logger module impoorted to log this 
import pandas as pd
# a powerful data analysis libraray to handle and manipulate data
from sklearn.model_selection import train_test_split
# a function from sklearn model to split the dataset into training and testing
from dataclasses import dataclass
# dataclasses module used to create a class that primarily stores data without writing explicit boilerplate code.

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass 

# this class holds the paths where the data files will be stored
class DataIngestionConfig:
    train_data_path : str=os.path.join("artifacts" , "train.csv")  # path for saving the training data
    test_data_path : str=os.path.join("artifacts" , "test.csv")    # path for saving the test data
    raw_data_path : str=os.path.join("artifacts" , "raw.csv")   # path for saving the raw data


# this class handle the actual data ingestion process
class DataIngestion:
    def __init__(self):  
        self.ingestion_config=DataIngestionConfig()
        # it is a method which initialize the dataingestion obj by creating an instance of dataingestionconfig which stores the path of the data files
        print("Train data path:", self.ingestion_config.train_data_path)
        print("Test data path:", self.ingestion_config.test_data_path)
        print("Raw data path:", self.ingestion_config.raw_data_path)



    def initiate_data_ingestion(self):
        logging.info("Enter the Data Ingestion method or component")
        try:
            dataset = pd.read_csv("notebook\data\cleaned_data.csv")
            logging.info("Read the datasets as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            #Creates directories (if they don't already exist) for saving the train and test data files. The directories are derived from the paths specified in DataIngestionConfig.
            dataset.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            #Saves the entire dataset as raw.csv in the artifacts directory.
            logging.info("Train Test Split Initiated")
            train , test = train_test_split(dataset , test_size=0.2,random_state=42)

            train.to_csv(self.ingestion_config.train_data_path , index=False,header=True)
            test.to_csv(self.ingestion_config.test_data_path , index=False,header=True)

            logging.info("Ingestion of the Data is Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,

            )

            
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data , test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)

    """

        Purpose: The script ingests a dataset, splits it into training and testing sets, and saves them as CSV files in specified locations.
Error Handling: The script uses a custom exception class (CustomException) to handle errors and logs messages throughout the process to provide information about the execution flow.
    """