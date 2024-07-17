import os
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.metrics import recall_score

from dataclasses import dataclass
from src.utils import save_file_as_pickle

@dataclass
class ModelTrainingConfig:
    model_pkl_path=os.path.join("artifacts/pickle","mdl.pkl")

class ModelTraining:
    def __init__(self):
        self.mdl_config=ModelTrainingConfig()

    def initiate_model_training(self,transform_train_dataset,transform_test_dataset):
        try:
            xtrain=transform_train_dataset[:,:-1]
            ytrain=transform_train_dataset[:,-1]

            xtest=transform_test_dataset[:,:-1]
            true_value=transform_test_dataset[:,-1]

            models={
                "Lr":LogisticRegression(),
                "SVC":SVC(),
                "DT":DecisionTreeClassifier(),
                "RTC":RandomForestClassifier(),
                "AB":AdaBoostClassifier(),
                "GB":GradientBoostingClassifier()
            }
            model_report={}

            for model_name,model in models.items():
                model.fit(xtrain,ytrain)
                predicted_value=model.predict(xtest)
                recall=recall_score(true_value,predicted_value)
                model_report[model_name]=recall

            best_model_name=max(model_report,key=model_report.get)

            best_model=models[best_model_name]
            save_file_as_pickle(self.mdl_config.model_pkl_path,best_model,"Model trainer")


        except Exception as e:
            raise e