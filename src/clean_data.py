import os

def inspect_data(df):

    print("========== MISSING VALUES ==========")
    print(df.isnull().sum())
    print("\n")
    print("========== DUPLICATE RECORDS ==========")
    print(df.duplicated().sum())
    print("\n")
    print("========== DESCRIPTIVE STATISTICS ==========")
    print(df.describe())
    print("\n")
    print("========== MEMORY USAGE ==========")
    memory = df.memory_usage(deep=True)
    print(memory)
    print("\n")
    print("========== DATASET INFO ==========")
    df.info()


def clean_data(df):

    df = df.drop_duplicates()

    df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

    df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100 )]
    df = df[(df["Marks"] >= 0) & (df["Marks"] <= 100 )]
    df = df[(df["StudyHours"] >= 0) & (df["StudyHours"] <= 24 )]

    df.to_csv("output/cleaned_data.csv", index = False)

    print("Cleaned data saved to output")

    return df