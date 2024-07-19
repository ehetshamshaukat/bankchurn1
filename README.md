
# About
```requirements
Churn prediction of US bank 
imbalance dataset 
Classification model
```

# Environment

#### 1. Create environment
```requirements
conda create -p venv python==3.10 -y
```

#### 2. Activate environment
```requirements
conda activate venv/
```
# Code
## 1. Components
#### a. Data Ingestion
```requirements
reading and splitting data into train and test dataset
```
#### b. Data Transformation
```requirements
reading train and test dataset for transformation and save in config as pickle format 
```

#### c. Model training
```requirements
using transformed train and test dataset for model training and saving best model in pickle format  
```

## 2. Pipeline
#### a. training pipeline
```requirements
pipeline for model training 
```
#### b. prediction pipeline
```requirements
pipeline for prediction using pickle file 
```


# Application
```requirements
streamlit run application.py
```


# Docker
#### 1. building image
```requirements
docker build -t image_name .
```

#### 2. running image
```requirements
docker run image_name 
```
