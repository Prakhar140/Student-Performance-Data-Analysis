from src.load_data import load_data, display_data
from src.clean_data import inspect_data, clean_data
from src.transform import transform_data, filter_data
from src.analyze import analyze_data

def main():
    df = load_data()

    display_data(df)

    inspect_data(df)

    df = clean_data(df)

    df = transform_data(df)   # Creates Grade, Result, Performance Score

    filter_data(df)

    analyze_data(df)

if __name__ == "__main__":
    main()