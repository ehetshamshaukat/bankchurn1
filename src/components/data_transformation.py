import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
import os

from src.utils import save_file_as_pickle


@dataclass
class DataTransformationConfig:
    data_transformation_pickle_path = os.path.join("artifacts/pickle", "dt.pkl")


class DataTransformation:
    def __init__(self):
        self.dt_pickle_path = DataTransformationConfig()

    def transformation(self):
        try:
            numerical_columns = ['creditscore', 'age', 'tenure', 'balance', 'estimatedsalary']
            categorical_columns = ['country', 'gender', 'hascrcard', 'isactivemember']

            numerical_column_pipeline = Pipeline([
                ("impute", SimpleImputer(strategy="median")),
                ("standard_scaler", StandardScaler())
            ])
            categorical_column_pipeline = Pipeline([
                ("impute", SimpleImputer(strategy="most_frequent")),
                ("encoder", OrdinalEncoder()),
                ("standard_scaler", StandardScaler())
            ])

            preprocessing = ColumnTransformer([
                ("numerical_column_pipeline", numerical_column_pipeline, numerical_columns),
                ("categorical_column_pipeline", categorical_column_pipeline, categorical_columns)
            ])

            return preprocessing
        except Exception as e:
            raise e

    def initiate_data_transformation(self, train_df, test_df):
        try:
            train_dataset = pd.read_csv(train_df)
            print(train_dataset)
            test_dataset = pd.read_csv(test_df)

            columns_to_drop = "exited"
            target_column = "exited"

            xtrain = train_dataset.drop(columns=columns_to_drop, axis=1)
            print(xtrain)
            ytrain = train_dataset[target_column]

            xtest = test_dataset.drop(columns=columns_to_drop, axis=1)
            ytest = test_dataset[target_column]

            dt = self.transformation()
            transformed_xtrain = dt.fit_transform(xtrain)
            transformed_xtest = dt.transform(xtest)

            transform_train = np.c_[transformed_xtrain, np.array(ytrain)]
            transform_test = np.c_[transformed_xtest, np.array(ytest)]

            save_file_as_pickle(self.dt_pickle_path.data_transformation_pickle_path, dt,"DataTransformation")

            return transform_train, transform_test

        except Exception as e:
            raise e
