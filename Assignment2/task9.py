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
