import matplotlib.pyplot as plt

def plot_grade_distribution(df):

    grade_count = df["Grade"].value_counts()

    plt.figure(figsize=(6,4))
    grade_count.plot(kind="bar")

    plt.title("Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.savefig("output/grade_distribution.png")

    plt.show()