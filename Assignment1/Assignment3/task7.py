# Task 7: Pattern heatmap 
# • Create a table with continents as rows and years as columns showing average life expectancy: 
# pivot = gap.pivot_table(index="continent", columns="year", values="lifeExp", 
# aggfunc="mean") 
# • Draw it with sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu"). 
# • Which continent has the lowest values throughout? In which years does the colour change 
# fastest? 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Gapminder dataset
gap = px.data.gapminder()

gap_2007 = gap[gap["year"] == 2007]
pivot = gap.pivot_table(index="continent", columns="year", values="lifeExp", 
aggfunc="mean") 

# Step:1 
gap.head()
data = gap_2007[
    ["lifeExp", "pop", "gdpPercap"]]

# Step-2: Calculate the correlation
corr_matrix = data.corr()
print(corr_matrix)
# Step-3: Draw the heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    pivot,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu" 
)
plt.title("Pattern Heatmap (2007)")
plt.tight_layout()
plt.show()