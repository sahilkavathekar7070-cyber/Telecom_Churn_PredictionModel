import pandas as pd

def data_ingestion():
    '''
    Title : Telecom Customer Churn Prediction Model

    Independent Columns[X] :'customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
       'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod', 'MonthlyCharges', 'TotalCharges'

    Target Column[y] : 'Churn'

    Problem Statement :
    1. To predict churn rate
    2. Use clustering approach to predict and classify the cluster pattern such as {l1,l2,l3}
    '''
    df = pd.read_csv(r'C:\Telecom_Churn_PredictionModel\data\raw\churn.csv')
    return df