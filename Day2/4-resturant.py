import matplotlib.pyplot as plt

salaries = [
    25000, 30000, 32000, 35000, 38000, 40000,
    42000, 45000, 48000, 50000, 52000, 55000,
    60000, 65000, 70000
]

plt.figure(figsize=(8, 5))

plt.hist(
    salaries,
    bins=5,
    color="skyblue",
    edgecolor="black"
)

plt.title("Employee Salary Distribution")
plt.xlabel("MOnthly Salary (Rs.)")
plt.ylabel("Number of Employee")

plt.show()