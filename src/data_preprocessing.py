def data_preprocessing(df):
    # step 1 : Drop duplicated values
    # step 2 : Feature engineering (optional)
    # step 3 : Split the dataset into independent [X] and dependent[y]
    # step 4 : Split the dataset into train and test data
    # step 5 : Build EnE Pipeline for numerical and categorical
    # step 6 : Build numerical pipeline with imputation and scaling
    # step 7 : Build categorical pipeline with imputation and encoding
    # step 8 : Concat numerical and categorical pipeline with ColumnTransformer
    # step 9 : fit transformer on train and test
    # step 10 : Return the preprocess train and test : X_train,X_test,y_train,y_test