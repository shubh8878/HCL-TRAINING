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

# Task 11: Hypothesis test on two groups
# Compare marks of CSE and ECE students

# H0: Average marks of CSE and ECE are equal
# H1: Average marks of CSE and ECE are different

cse_marks = df[df["Branch"] == "CSE"]["Marks"]
ece_marks = df[df["Branch"] == "ECE"]["Marks"]

print("CSE Students:", len(cse_marks))
print("ECE Students:", len(ece_marks))

print("CSE Average Marks:", cse_marks.mean())
print("ECE Average Marks:", ece_marks.mean())

t_stat, p_value = stats.ttest_ind(
    cse_marks,
    ece_marks,
    equal_var=False
)

print("\nT-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Decision: Reject H0")
    print("Conclusion: There is a significant difference between the two groups.")
else:
    print("Decision: Fail to reject H0")
    print("Conclusion: There is not enough evidence of a significant difference.")