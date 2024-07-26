# Project: Bank Churn Prediction
## Problem statement
### 1. Goal
```
To predict the price of ride 
```
### 2. About churn prediction
```requirements
Predicting customer churn is crucial for businesses aiming to retain customers and reduce losses. By identifying customers likely to leave, companies can implement strategies to improve retention. This project focuses on developing a predictive model using machine learning techniques to identify at-risk customers
```
## Description
### 1. Dataset
```
1. Bank churn prediction is about predicting whether a customer is going to leave or stay base on different sceniro such as having low balance or customer is active or not 
2. Imabalance dataset, mean one category is way more than other category 
3. Dataset available on kaggle 
```

### 2. Features
``` 
Input features = [creditscore, country, gender, age, tenure, balance, hascrcard, isactivemember, estimatedsalary]
Target feature = [exited]
```
### 3. Pipeline Structure
```requirements
Google define pipeline 
```
# Requirements
### 1. Language
```
Python 3.10
```
### 2. Libraries
```
1. numpy
2. pandas
3. scikit-learn
4. pickle
5. os 
6. streamlit 
 ```
# code
### 1. Enviroment
```requirements
conda create -p venv python==3.10 -y 
```
### 2. Activate enviroment
```requirements
conda activate venv/
```
### 3. Setup
```
The setup.py is a Python script typically included with Python-written libraries or apps. Its objective is to ensure that the program is installed correctly. 
```
### 4. Components
- Data ingestion
```
reading data from different source and splitting data into train and test
```
- Data transformation
```
  reading train and test dataset and apply different transformation and save transformation setting in pickle format
```
- Model training
```requirements
transformed dataset and using different machine learning model and save the best model in pickle format
```
### 5. Pipeline
- Training pipeline
```
using components and creating pipeline for model training
```
- Prediction pipeline
```
taking data from user transform for model and predict 
```

## Run
#### 1. Download repository
```
git clone https://github.com/ehetshamshaukat/bankchurn1.git
```
#### 2. Install dependences
```requirements
pip install -r requirements.txt
```
#### 3. Transformation and training
- data transformation and model training
  ```
  For model training, which will also save tranformation and model in pickle format
  python src/pipeline/training_pipeline.py
  ```
- Prediction
  ```
  For Prediction on new data
  python src/pipeline/prediction_pipeline.py
  ```
#### 4. Streamlit  
```
to predict
streamlit run application.py
```
## Deployment
```
Deploy on AWS using Github actions which is CI CD technique
```
## Image
<img width="1507" alt="Screenshot 2024-07-24 at 4 08 39 PM" src="https://github.com/user-attachments/assets/f67a21bb-fb00-46f3-beda-c8f71b600159">

