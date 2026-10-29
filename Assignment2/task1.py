import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()    # Restaurant bills and tips
iris = px.data.iris()    # Flower measurements
stocks = px.data.stocks() # Weekly stock prices

print(tips.head())

# Task 1: Line chart 
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
# sales = [12, 15, 14, 20, 24, 22]   # in thousands 
# • Draw a line chart of sales against months using plt.plot() with circle markers and a grid. 
# • Add a title, an x-axis label and a y-axis label. 
# • Which month had the highest sales? 

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 20, 24, 22]  # Sales in thousands

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales,
    marker="o",
    color="blue",
    label="Monthly Sales"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales (Thousands)")
plt.grid(True)

plt.show()