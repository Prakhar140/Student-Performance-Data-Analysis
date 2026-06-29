import pandas as pd

def generate_report(df):

    report = {
        "Total Students": len(df),
        "Passed Students" : (df["Result"] == "Pass").sum(),
        "Failed Students" : (df["Result"] == "Fail").sum(),
        "Highest Marks": df["Marks"].max(),
        "Lowest Marks": df["Marks"].min(),
        "Average Marks": df["Marks"].mean(),
        "Average Attendance": df["Attendance"].mean(),
       
    }

    report_df = pd.DataFrame(report, index=[0])

    grade_distribution = (
        df["Grade"]
        .value_counts()
        .rename_axis("Grade")
        .reset_index(name="Count")
    )

    report_df.to_csv("output/report.csv", index=False)
    grade_distribution.to_csv("output/grade_distribution.csv", index=False)

    print("\n✅Report generated successfully.")
   
    print("\n")