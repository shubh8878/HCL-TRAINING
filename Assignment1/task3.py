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

# Task 3: Flexible functions 
# • Write a function summary(*values, round_to=2) that accepts any number of values and returns a dictionary with the count, minimum, maximum and average. 
# • Test it with summary(10, 20, 30) and with summary(*df["Marks"]).

def summary(*values, round_to=2):

    #handle empty input
    if len (values) == 0:
        return {"count": 0, "min": None, "max": None, "average": None}
    results = {
        "Count": len(values),
        "Min": min(values),
        "Max": max(values),
        "Average": round(sum(values) / len(values), round_to)
    }
    return results

#test 1 
print (summary(10, 20, 30))

#test 2
print(summary(*df["Marks"]))