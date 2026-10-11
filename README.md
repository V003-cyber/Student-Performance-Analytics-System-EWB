# Student Performance Analytics System

**Course:** Python with AI  
**Submitted By:** Varenya Kushwaha 
**Submission Date:** October 2026  

---

## 1. Project Title
**Student Performance Analytics System**

## 2. Objective
The objective of this project is to build a automated data processing and analytical tool in Python to evaluate student academic performance. The system loads student datasets, performs key mathematical operations using NumPy, manipulates structured data using Pandas, and generates actionable insights such as subject-wise metrics, individual student grades, overall pass/fail statistics, and top performers.

## 3. Technologies Used
* **Programming Language:** Python 3.x
* **Data Processing & Analysis:** Pandas, NumPy
* **Version Control & Repository:** Git, GitHub

## 4. Dataset Description
The dataset (`students.csv`) consists of 18 individual student records with performance across core subjects and attendance data:
* **Student_ID:** Unique numeric identifier for each student.
* **Name:** Full name of the student.
* **Department:** Academic discipline (e.g., CS, ECE, ME).
* **Maths, Physics, Chemistry:** Numeric scores obtained in respective subjects (out of 100).
* **Attendance:** Percentage of classes attended.

## 5. Implementation
The project follows a modular structure separated into data handling, functional processing, and user output execution:
1. **Data Loading:** Pandas (`pd.read_csv`) reads and structures the dataset into a DataFrame.
2. **Vectorized Calculations:** NumPy (`np.sum`, `np.mean`) calculates total marks and average scores efficiently across subject vectors.
3. **Iterative Evaluation:** A Python `for` loop iterates through records to apply passing rules ($\text{Average} \ge 40$ and all subject scores $\ge 35$) and assigns corresponding academic grades (A+, A, B, C, F).
4. **Statistical Summaries:** NumPy aggregate functions compute summary statistics (highest, lowest, overall average) across subjects and class cohorts.

## 6. Key Features
* **Automated Data Ingestion:** Safely loads CSV dataset with error checking.
* **Calculated Grade Metrics:** Computes individual totals, averages, pass/fail status, and letter grades.
* **Subject-Wise Analytics:** Generates min, max, and mean scores across Maths, Physics, and Chemistry.
* **Class Health Dashboard:** Summarizes class pass percentage, average attendance, and overall mean score.
* **Leaderboard Identification:** Sorts and displays top-ranking performers.

## 7. Output Overview
When `main.py` is executed, the system displays the following organized sections in the console terminal:
* Complete tabular view of processed student records with computed grades and status.
* Statistical summary key-value indicators (Pass Percentage, Attendance, Average).
* Subject-wise performance summary table.
* Top 3 high-performing students.

## 8. Final Outcome
The application successfully processes unstructured student data and produces immediate analytical insights without requiring manual calculation. It demonstrates practical usage of foundational Python loops, reusable functions, Pandas DataFrame manipulation, and NumPy array computations.

## 9. Challenges & Learning
* **Challenges:** Structuring logic to evaluate multiple pass criteria across individual subjects alongside aggregate average scores.
* **Learning:** Gained hands-on experience in using NumPy vector operations for row-wise processing, organizing standard multi-file Python projects, and setting up automated analytical workflows.
