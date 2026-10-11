from functions import (
    calculate_student_metrics,
    get_class_summary,
    get_subject_performance,
    get_top_performers,
    load_data,
)


def main():
    print("=" * 60)
    print("      STUDENT PERFORMANCE ANALYTICS SYSTEM      ")
    print("=" * 60)

    # 1. Load Data
    data_path = "student.csv"
    df = load_data(data_path)

    if df is None or df.empty:
        print("Failed to load records. Exiting system.")
        return

    # 2. Process Data
    df = calculate_student_metrics(df)

    # 3. Display Detailed Processed Table
    print("\n--- Processed Student Records ---")
    print(
        df[
            [
                "Student_ID",
                "Name",
                "Department",
                "Total",
                "Average",
                "Grade",
                "Status",
            ]
        ].to_string(index=False)
    )

    # 4. Overall Class Summary
    print("\n--- Class Performance Summary ---")
    summary = get_class_summary(df)
    for key, value in summary.items():
        print(f"{key:<25}: {value}")

    # 5. Subject-Wise Analysis
    print("\n--- Subject-Wise Performance Analysis ---")
    subject_df = get_subject_performance(df)
    print(subject_df.to_string())

    # 6. Top Performers
    print("\n--- Top Performers ---")
    top_students = get_top_performers(df, top_n=3)
    print(top_students.to_string(index=False))

    print("\n=" + "=" * 60)
    print("Analysis Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()