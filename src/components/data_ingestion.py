import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:

    def __init__(self):
        self.config = DataIngestionConfig()

    def load_data(self):
        logging.info("Entering initiate_data_ingestion method")
        try:
            df = pd.read_csv("notebooks/data/stud.csv")
            logging.info("Read the dataset as DataFrame")

            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)

            df.to_csv(self.config.raw_data_path, index=False, header=True)

            logging.info("Saved the raw data to artifacts folder")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)

            logging.info("Ingestion completed successfully.")

            return (
                self.config.train_data_path,
                self.config.test_data_path,
            )

        except Exception as e:
            ex = CustomException(e, sys)
            logging.error(ex.error_message)
            raise ex
