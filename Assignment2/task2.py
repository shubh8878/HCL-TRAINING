# Task 2: Bar chart
# • Find the average tip for each day: avg_tip = tips.groupby("day")
# ["tip"].mean().reindex(["Thur", "Fri", "Sat", "Sun"])
# • Draw a bar chart using plt.bar() with a colour of your choice.
# tips.head()
# Dataset What it contains
# tips 244 restaurant bills: total_bill, tip, sex,
# smoker, day, time, size (people at the table)
# iris 150 flowers: sepal and petal measurements
# and the species
# stocks
# Weekly prices of 6 companies for 2018 to
# 2019, shown relative to the first week (1.0 =
# starting price)
# • On which day are tips the highest?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
tips = px.data.tips() # restaurant bills and tips
iris = px.data.iris() # flower measurements
stocks = px.data.stocks() # weekly stock prices
tips.head()

tips = px.data.tips()

avg_tip = tips.groupby("day")["tip"].mean()
avg_tip = avg_tip.reindex(["Thur", "Fri", "Sat", "Sun"])

plt.figure(figsize=(8, 5))
plt.bar(avg_tip.index, avg_tip.values, color="skyblue")

plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip ($)")
plt.tight_layout()
plt.show()

print(avg_tip)