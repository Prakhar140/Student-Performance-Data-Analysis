from src.load_data import load_data, display_data
from src.clean_data import inspect_data, clean_data
from src.transform import transform_data, filter_data
from src.analyze import analyze_data, sort_data, group_data
from src.analyze import(
    analyze_data,
    sort_data,
    group_data,
    statistical_analysis
)
from src.report import generate_report

def main():
    print("====== Student Performance Data Analysis ======")
    print("\n")

    df = load_data()

    display_data(df)

    inspect_data(df)

    df = clean_data(df)

    df = transform_data(df)   # Creates Grade, Result, Performance Score

    filter_data(df)

    analyze_data(df)

    sort_data(df)

    group_data(df)

    statistical_analysis(df)

    generate_report(df)

if __name__ == "__main__":
    main()