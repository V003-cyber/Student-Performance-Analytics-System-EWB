import numpy as np
import pandas as pd


def load_data(file_path):
    """Loads student dataset into a Pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print("Data successfully loaded!")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def calculate_student_metrics(df):
    """Calculates total marks, average marks, grades, and pass/fail status."""
    subjects = ["Maths", "Physics", "Chemistry"]

    # NumPy vector operations for calculating total and average marks
    marks_array = df[subjects].values
    df["Total"] = np.sum(marks_array, axis=1)
    df["Average"] = np.mean(marks_array, axis=1)

    # Calculate Pass/Fail status using loop (Pass condition: Average >= 40 and each subject >= 35)
    status_list = []
    grade_list = []

    for index, row in df.iterrows():
        # Pass condition check
        if (
            row["Average"] >= 40
            and row["Maths"] >= 35
            and row["Physics"] >= 35
            and row["Chemistry"] >= 35
        ):
            status_list.append("Pass")
        else:
            status_list.append("Fail")

        # Grading logic
        avg = row["Average"]
        if avg >= 85:
            grade_list.append("A+")
        elif avg >= 75:
            grade_list.append("A")
        elif avg >= 60:
            grade_list.append("B")
        elif avg >= 40:
            grade_list.append("C")
        else:
            grade_list.append("F")

    df["Status"] = status_list
    df["Grade"] = grade_list
    return df


def get_class_summary(df):
    """Generates overall class performance metrics."""
    total_students = len(df)
    passed_students = len(df[df["Status"] == "Pass"])
    failed_students = len(df[df["Status"] == "Fail"])

    # Using NumPy to get mean average mark and attendance
    overall_avg = np.mean(df["Average"].values)
    avg_attendance = np.mean(df["Attendance"].values)

    summary = {
        "Total Students": total_students,
        "Passed": passed_students,
        "Failed": failed_students,
        "Pass Percentage": round((passed_students / total_students) * 100, 2),
        "Overall Class Average": round(overall_avg, 2),
        "Average Attendance (%)": round(avg_attendance, 2),
    }
    return summary


def get_subject_performance(df):
    """Generates subject-wise performance analysis using NumPy and Pandas."""
    subjects = ["Maths", "Physics", "Chemistry"]
    subject_stats = {}

    for subject in subjects:
        scores = df[subject].values
        subject_stats[subject] = {
            "Average": round(np.mean(scores), 2),
            "Highest": np.max(scores),
            "Lowest": np.min(scores),
        }

    return pd.DataFrame(subject_stats).T


def get_top_performers(df, top_n=3):
    """Returns top performing students based on average score."""
    sorted_df = df.sort_values(by="Average", ascending=False)
    return sorted_df[["Student_ID", "Name", "Department", "Average", "Grade"]].head(top_n)