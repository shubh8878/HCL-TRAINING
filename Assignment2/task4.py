# Task 4: Count plot and bar plot
# •	Draw sns.countplot(data=tips, x="day") to show the number of customers on each day.
# •	Draw sns.barplot(data=tips, x="day", y="total_bill") to show the average bill on each day.
# •	Which day has the most customers? Which day has the highest average bill?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()      # restaurant bills and tips
iris = px.data.iris()      # flower measurements
stocks = px.data.stocks()  # weekly stock prices

tips.head()

plt.figure(figsize=(8,5))

sns.countplot(
    data=tips,
    x="day",
    order = ["Thur","Fri","Sat","Sun"],
    color="orange"
)

plt.title("Number of customers by Day")
plt.xlabel("Day")
plt.ylabel("Number of Recorders")

plt.show()

plt.figure(figsize=(8, 5))

sns.barplot(
    data=tips,
    x="day",
    y="total_bill",
    order=["Thur", "Fri", "Sat", "Sun"],
    color="teal"
)

plt.title("Average Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Bill ($)")
plt.show()

avg_bills = tips.groupby("day")["total_bill"].mean()
print(avg_bills)
print("Highest Average Bill: Day: ", avg_bills.idxmax())