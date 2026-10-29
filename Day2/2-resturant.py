import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()
print(tips.head())

regions = ["North", "South", "East", "west", "Central"]
Sales = [50000, 65000, 40000, 70000, 55000]

plt.bar(regions, Sales, color="skyblue")

plt.title("region-wise Sales Comparison")
plt.xlabel("regions")
plt.ylabel("Sales (Rs.)")

plt.show()