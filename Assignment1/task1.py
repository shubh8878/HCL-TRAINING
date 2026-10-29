import numpy as np
import pandas as pd

np.random.seed(42)
n = 40
df = pd.DataFrame({
    "Student_ID": range(1, n + 1),
    "Branch": np.random.choice(["CSE", "ECE", "ME", "CE"], n),
    "Study_Hours": np.round(np.random.uniform(1, 8, n), 1),
    "Attendance": np.random.randint(55, 100, n),
})
df["Marks"] = np.clip(
    np.round(30 + 5 * df["Study_Hours"] + 0.2 * df["Attendance"] + np.random.normal(0, 6, n)),
    0, 100
).astype(int)

df.head()
print()


# Task 1: Grading function
# •	Write a function get_grade(marks) that returns "A" for 75 and above, "B" for 60 to 74, "C" for 40 to 59, and "F" below 40.
# •	Add a Grade column to df using apply().
# •	Show how many students got each grade using value_counts().
def get_grade(marks):
    if marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

# Add a Grade column using apply()
df["Grade"] = df["Marks"].apply(get_grade)

# Display the students with their marks and grades
print(df[["Student_ID", "Marks", "Grade"]])

# Count students in each grade
print(df["Grade"].value_counts())


