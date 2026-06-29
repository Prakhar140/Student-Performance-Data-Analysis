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

    print("\n")

    print("Grade Distribution:")
    print(df["Grade"].value_counts())

    print("\n")


def sort_data(df):

    print("============================ SORT BY MARKS ============================")
    sorted_df = df.sort_values(by="Marks", ascending=False)
    print(sorted_df)
    print("\n")

    print("========================= SORT BY ATTENDANCE ==========================")
    sorted_df = df.sort_values(by="Attendance", ascending=False)
    print(sorted_df)
    print("\n")

    print("========================= SORT BY STUDY HOURS =========================")
    sorted_df = df.sort_values(by="StudyHours", ascending=False)
    print(sorted_df)
    print("\n")


def group_data(df):

    print("========================= GROUP BY GRADE =========================")
    print("\n")
    print("Average Marks by Grade:")
    print(df.groupby("Grade")["Marks"].mean())

    print("\n")

    print("Number of students in each Grade:")
    print(df.groupby("Grade")["Grade"].count())

    print("\n")

    print("Average Attendance by Grade:")
    print(df.groupby("Grade")["Attendance"].mean())


def statistical_analysis(df):

    print("========================= STATISTICAL ANALYSIS =========================")
    print("\n")
    
    print("Mean : ")
    print(df[["Marks", "Attendance", "StudyHours"]].mean())
    print("\n")

    print("Mode : ")
    print(df[["Marks", "Attendance", "StudyHours"]].mode())
    print("\n")

    print("Median : ")
    print(df[["Marks", "Attendance", "StudyHours"]].median())
    print("\n")

    print("Standard Deviation : ")
    print(df[["Marks", "Attendance", "StudyHours"]].std())  
    print("\n")

    print("Variance : ")
    print(df[["Marks", "Attendance", "StudyHours"]].var())  
    print("\n")

    print("Correlation Matrix : ")
    print(df[["Marks", "Attendance", "StudyHours"]].corr())
    print("\n")