import os
import pandas as pd
from src.utils import load_pickle_file


class Prediction:
    def __init__(self):
        pass
    def initiate_prediction(self, feature):
        try:
            preprocessing_path = os.path.join("artifacts/pickle", "dt.pkl")
            model_path = os.path.join("artifacts/pickle", "mdl.pkl")

            preprocessing = load_pickle_file(preprocessing_path)
            model = load_pickle_file(model_path)

            processed_data = preprocessing.transform(feature)
            output = model.predict(processed_data)
            return output

        except Exception as e:
            raise e


class Features:
    def __init__(self, creditscore, country, gender, age, tenure, balance, hascrcard, isactivemember, estimatedsalary):
        self.creditscore = creditscore
        self.country = country
        self.gender = gender
        self.age = age
        self.tenure = tenure
        self.balance = balance
        self.hascrcard = hascrcard
        self.isactivemember = isactivemember
        self.estimatedsalary = estimatedsalary

    def to_dataframe(self):
        try:
            feature_as_dict = {
                'creditscore': [self.creditscore],
                'country': [self.country],
                'gender': [self.gender],
                'age': [self.age],
                'tenure': [self.tenure],
                'balance': [self.balance],
                'hascrcard': [self.hascrcard],
                'isactivemember': [self.isactivemember],
                'estimatedsalary': [self.estimatedsalary]
            }
            feature_as_df = pd.DataFrame(feature_as_dict)
            return feature_as_df
        except Exception as e:
            raise e
