import pandas as pd

def load_data(file_path="data/student_dataset_v2.csv"):
    df = pd.read_csv(file_path)
    return df


def display_data(df):
    print("============== FIRST 5 RECORDS ================")
    print(df.head())
    print("\n")
    print("=================== LAST 5 RECORDS ===================")
    print(df.tail())
    print("\n")
    print("========== DATASET SHAPE ==========")
    print(df.shape)
    print("\n")
    print("========== COLUMN NAMES ==========")
    print(df.columns)
    print("\n")
    print("========== DATA TYPES ==========")
    print(df.dtypes)
    print("\n")