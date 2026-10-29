# Task 3: Change over time
# 	•	Select the data of India, China, Brazil and United States using gap[gap["country"].isin([...])].
# 	•	Draw a line chart of lifeExp against year, one line per country, using sns.lineplot(..., hue="country", marker="o").
# 	•	Which country started with the lowest life expectancy and which one improved the fastest? Why is a line chart the right choice here?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

gap = px.data.gapminder()

countries=[
    "China",
    "India",
    "United States",
    "Brazil"
]
data=gap[gap["country"].isin(countries)]
plt.figure(figsize=(10, 6))

sns.lineplot(
    data=data,
    x="year",
    y="lifeExp",
    hue="country",
    marker="o"
)
plt.title("Life Expectancy Over Time for Selected Countries")
plt.xlabel("Year")
plt.ylabel("Life Expectancy")
plt.grid(True,alpha=0.3)
plt.legend(title="Country")

plt.tight_layout()
plt.show()