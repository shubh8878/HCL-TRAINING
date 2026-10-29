# Task 5: Box plot
# • Draw sns.boxplot(data=tips, x="day", y="total_bill").
# • Which day has the highest median bill? Are there dots beyond the whiskers? What do
# they represent?
# • Redraw the plot with hue="sex" added and note one difference you see.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
tips = px.data.tips() # restaurant bills and tips
iris = px.data.iris() # flower measurements
stocks = px.data.stocks() # weekly stock prices
tips.head()


sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    order = ["Thur","Fri","Sat","Sun"],
    color="lightblue"
)   
plt.title("Boxplot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()  

avg_bill_by_day = tips.groupby("day")["total_bill"].median()
print("Median total bill by day:")
print(avg_bill_by_day)  