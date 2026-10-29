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