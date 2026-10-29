# Task 10: Line chart with a range slider 
# • Draw px.line(stocks, x="date", y=["GOOG", "AAPL", "AMZN"]), then add 
# fig.update_xaxes(rangeslider_visible=True). 
# • Which of the three stocks grew the most by the end of 2019? 
# • Use the slider to zoom into any three-month period and note what happened there. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()    # Restaurant bills and tips
iris = px.data.iris()    # Flower measurements
stocks = px.data.stocks() # Weekly stock prices

(tips.head())

fig = px.line(
    stocks,
    x="date",
    y=["GOOG", "AAPL", "AMZN"],
    title="Stock Price Trends (2018–2019)"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Relative Stock Price",
    legend_title="Company"
)

fig.update_xaxes(rangeslider_visible=True)

fig.show()