# ask 1: Ranked bar chart
# 	•	From gap_2007, select the 10 countries with the largest population using nlargest(10, "pop").
# 	•	Draw a horizontal bar chart with plt.barh(), showing population in millions (divide pop by 1,000,000). Sort the data so the largest bar is at the top.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

gap = px.data.gapminder()

gap_2007 = gap[gap["year"] == 2007]


top10 = gap_2007.nlargest(10, "pop").copy()


top10["population_million"] = top10["pop"] / 1_000_000


top10 = top10.sort_values("population_million")


plt.figure(figsize=(10, 6))

plt.barh(
    top10["country"],
    top10["population_million"],
    color="skyblue"
)

plt.xlabel("Population (millions)")
plt.ylabel("Country")
plt.title("Top 10 Most Populous Countries in 2007")

plt.tight_layout()
plt.show()