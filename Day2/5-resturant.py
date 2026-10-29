import matplotlib.pyplot as plt

# Sample salary data for three departments
salary_data = [
    [45000, 50000, 55000, 60000, 65000],
    [30000, 35000, 40000, 42000, 45000],
    [40000, 50000, 60000, 70000, 80000]
]

plt.figure(figsize=(8, 5))

plt.boxplot(
    salary_data,
    patch_artist=True,
    tick_labels=['IT', 'HR', 'Finance'],
    boxprops=dict(facecolor='lightblue', color='blue'),
    whiskerprops=dict(color='blue'),
    capprops=dict(color='blue'),
    medianprops=dict(color='red')
)

plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary (Rs.)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()