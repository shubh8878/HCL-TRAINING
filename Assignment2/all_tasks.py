

# ==================== TASK 1 ====================

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


# ==================== TASK 2 ====================

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


# ==================== TASK 3 ====================

# ask 3: Histogram and scatter plot side by side
# 	•	Create two charts in one figure using fig, axes = plt.subplots(1, 2, figsize=(12, 4)).
# 	•	On the left, draw a histogram of total_bill with 10 bins using axes[0].hist().
# 	•	On the right, draw a scatter plot of total_bill (x) against tip (y) using axes[1].scatter().
# 	•	Give each chart a title and axis labels using set_title(), set_xlabel() and set_ylabel().
# 	•	Save the figure with plt.savefig("tips_plots.png", dpi=150).
# 	•	In 2 lines, describe the most common bill range and the relationship between bill and tip.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
tips = px.data.tips() # restaurant bills and tips
iris = px.data.iris() # flower measurements
stocks = px.data.stocks() # weekly stock prices
tips.head()


# Task 3: Histogram and scatter plot side by side

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()

# Create two charts side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Histogram
axes[0].hist(tips["total_bill"], bins=10, color="skyblue")
axes[0].set_title("Histogram of Total Bill")
axes[0].set_xlabel("Total Bill")
axes[0].set_ylabel("Frequency")

# Scatter plot
axes[1].scatter(tips["total_bill"], tips["tip"], color="orange")
axes[1].set_title("Total Bill vs Tip")
axes[1].set_xlabel("Total Bill")
axes[1].set_ylabel("Tip")

# Save and display figure
plt.tight_layout()
plt.savefig("tips_plots.png", dpi=150)
plt.show()

# Observation
print("Most bills are generally in the range of 10 to 20.")
print("As the total bill increases, the tip generally also increases.")



# ==================== TASK 4 ====================

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


# ==================== TASK 5 ====================

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


# ==================== TASK 6 ====================

# Task 6: Scatter plot with colour and style 
# • Draw sns.scatterplot(data=tips, x="total_bill", y="tip", hue="smoker", 
# style="time"). 
# • In one line, say whether smokers and non-smokers tip differently.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()    # Restaurant bills and tips
iris = px.data.iris()    # Flower measurements
stocks = px.data.stocks() # Weekly stock prices

(tips.head())

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="smoker",
    style="time"
)

plt.title("Total Bill vs Tip by Smoking Status and Time")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.tight_layout()
plt.show()


# ==================== TASK 7 ====================

# Task 7: Pair plot 
# • Draw sns.pairplot(iris, hue="species", vars=["sepal_length", "sepal_width", 
# "petal_length", "petal_width"]). 
# • Which two measurements separate the three species best? Which species is the easiest to 
# identify?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()    # Restaurant bills and tips
iris = px.data.iris()    # Flower measurements
stocks = px.data.stocks() # Weekly stock prices

(tips.head())

sns.pairplot(
    iris,
    hue = "species",
    vars = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
)

plt.show()


# ==================== TASK 8 ====================

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


# ==================== TASK 9 ====================

# Task 9: Interactive box plot and histogram
# • Draw px.box(tips, x="day", y="total_bill", color="sex").
# • Draw px.histogram(tips, x="total_bill", color="time", nbins=15).
# • Which meal, Lunch or Dinner, has larger bills in general?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
tips = px.data.tips() # restaurant bills and tips
iris = px.data.iris() # flower measurements
stocks = px.data.stocks() # weekly stock prices
tips.head()


# Task 9: Interactive box plot and histogram

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()

# Box plot
fig1 = px.box(tips, x="day", y="total_bill", color="sex")
fig1.show()

# Histogram
fig2 = px.histogram(tips, x="total_bill", color="time", nbins=15)
fig2.show()

# Compare Lunch and Dinner bills
print(tips.groupby("time")["total_bill"].mean())

print("Dinner generally has larger bills than Lunch.")



# ==================== TASK 10 ====================

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


# ==================== TASK 11 ====================

# Task 11: Copy this table into a Markdown cell and complete it based on what you experienced.   
# Then write 2 to 3 lines: which library would you choose for a chart in a lab report, and which for a chart 
# on a web page? Give a reason for each.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()    # Restaurant bills and tips
iris = px.data.iris()    # Flower measurements
stocks = px.data.stocks() # Weekly stock prices

(tips.head())

comparison_data = {
    "Library": ["Matplotlib", "Seaborn", "Plotly"],
    "Ease of use (easy / medium / hard)": ["Medium", "Easy", "Medium"],
    "Interactive charts? (yes / no)": ["No", "No", "Yes"],
    "Best used for": [
        "Fine-grained customization & static plots", 
        "Statistical data visualization", 
        "Interactive dashboards & web apps"
    ]
}

comparison_df = pd.DataFrame(comparison_data)

print("\n--- Task 11: Library Comparison Table ---")
print(comparison_df.to_string(index=False))
