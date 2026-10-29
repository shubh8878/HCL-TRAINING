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
