from src.student_performance_predictor.logger import logging
from src.student_performance_predictor.exception import CustomException
from src.student_performance_predictor.components.data_ingestion import DataIngestion
import sys


if __name__ == '__main__':
    logging.info("The execution has started")

    try:
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()


    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)