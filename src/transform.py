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
        if marks >= 40:
            result.append("Pass")
        else:
            result.append("Fail")


    df["Result"] = result

    df["PerformanceScore"] = (
        df["Marks"] * 0.6 + df["Attendance"] * 0.2 + df["StudyHours"] * 2
    )

    
    return df