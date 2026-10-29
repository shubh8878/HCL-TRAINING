# Task 8: Interactive scatter plot 
# • Create the chart and display it with fig.show(): 
# fig = px.scatter(tips, x="total_bill", y="tip", color="day", size="size", 
# hover_data=["sex", "time"], title="Bill vs Tip") 
# fig.show() 
# • Hover over points, zoom into an area, and click a day in the legend to hide it. 
# • Write two things you can do in this chart that you could not do in your Matplotlib charts.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()    # Restaurant bills and tips
iris = px.data.iris()    # Flower measurements
stocks = px.data.stocks() # Weekly stock prices

(tips.head())

fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    color="day",
    size="size",
    hover_data=["sex", "time"],
    title="Bill vs Tip"
)

fig.show()