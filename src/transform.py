def transform_data(df):

    grade = []

    for marks in df["Marks"]:
        if marks >= 90:
            grade.append("A")
        elif marks >= 80:
            grade.append("B")
        elif marks >= 70:
            grade.append("C")
        elif marks >= 60:
            grade.append("D")
        else:
            grade.append("F")
    
    df["Grade"] = grade

    result = []

    for marks in df["Marks"]:
        if marks >= 50:
            result.append("Pass")
        else:
            result.append("Fail")


    df["Result"] = result

    df["PerformanceScore"] = (
        df["Marks"] * 0.6 + df["Attendance"] * 0.2 + df["StudyHours"] * 2
    )

    return df


def filter_data(df):

    toppers = df[df["Grade"] == "A"]
    
    failed = df[df["Result"] == "Fail"]

    low_attendance = df[df["Attendance"] < 75]

    high_study_hours = df[df["StudyHours"] > 8]

    toppers.to_csv("output/toppers.csv", index=False)
    failed.to_csv("output/failed_students.csv", index=False)
    low_attendance.to_csv("output/low_attendance.csv", index=False)
    high_study_hours.to_csv("output/high_study_hours.csv", index=False)

    print("✅Filtered data saved to output")
    print("\n")

    return df