from src.data_ingestion import data_ingestion

def main():
    # Step 1 : Data ingestion
    df= data_ingestion()
    print(df.columns)

    # Step 2 : Data Preprocessing


main()