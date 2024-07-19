import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os

@dataclass
class DataIngestionConfig:
    train_dataset_path = os.path.join("artifacts/train_test_dataset", "train.csv")
    test_dataset_path = os.path.join("artifacts/train_test_dataset", "test_csv")


class DataIngestion:
    def __init__(self):
        self.dataset = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            path = "dataset/bank_churn_prediction.csv"
            df = pd.read_csv(path)

            os.makedirs(os.path.dirname(self.dataset.train_dataset_path), exist_ok=True)

            train_dataset, test_dataset = train_test_split(df, test_size=0.33, random_state=69)

            train_dataset.to_csv(self.dataset.train_dataset_path, index=False, header=True)
            test_dataset.to_csv(self.dataset.test_dataset_path, index=False, header=True)

            return self.dataset.train_dataset_path, self.dataset.test_dataset_path

        except Exception as e:
            raise e
