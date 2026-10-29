import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()
print(tips.head())

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [25000, 30000, 28000, 35000, 40000, 45000]

plt.plot(months, sales, marker="o", color="blue")

plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales (Rs.)")

plt.grid(True)
plt.show()