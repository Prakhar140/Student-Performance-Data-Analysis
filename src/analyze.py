def analyze_data(df):

    print("========== DATA ANALYSIS ==========")
    print("Average Marks:", df["Marks"].mean())
    print("Highest Marks:", df["Marks"].max())
    print("Lowest Marks:", df["Marks"].min())

    print("\n")

    print("Average Attendance:", df["Attendance"].mean())
    
    print("Average Study Hours:", df["StudyHours"].mean())

    print("\n")

    pass_percentage = (df["Result"] == "Pass").mean() * 100
    print(f"Pass Percentage: {pass_percentage:.2f}%")

    fail_percentage = (df["Result"] == "Fail").mean() * 100
    print(f"Fail Percentage: {fail_percentage:.2f}%")

    print("Grade Distribution:")
    print(df["Grade"].value_counts())

    print("\n")
