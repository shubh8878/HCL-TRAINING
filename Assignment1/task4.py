import numpy as np
import pandas as pd
from scipy import stats 

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

# Task 4: Safe file handling 
# • Save df to a file named students.csv using to_csv(index=False). 
# • Write a function load_data(filename) that reads a CSV file using try and except. If the file is not found, it should print a friendly message instead of crashing. 
# • Test it once with the correct file name and once with a wrong name. 

# 1. Save the DataFrame to a CSV file
df.to_csv("students.csv", index=False)
print("Data saved successfully!")

# 2. Function to load data safely
def load_data(filename):
    try:
        data = pd.read_csv(filename)
        print("File loaded successfully!")
        return data

    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")
        return None

# 3. Test with the correct filename
data = load_data("students.csv")
print(data)

# 4. Test with an incorrect filename
data2 = load_data("wrong.csv")