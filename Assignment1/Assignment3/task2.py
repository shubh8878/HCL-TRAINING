# Task 2: Grouped bar chart
# 	•	Create a table of the average life expectancy of each continent for the years 1952 and 2007:
# g = gap[gap["year"].isin([1952, 2007])].groupby(["continent", "year"])["lifeExp"].mean().unstack()
# 	•	Draw it as a grouped bar chart using g.plot(kind="bar").
# 	•	Which continent improved the most between 1952 and 2007?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Gapminder dataset
gap = px.data.gapminder()

# Select data for 1952 and 2007
data = gap[gap["year"].isin([1952, 2007])]

# Calculate average life expectancy by continent and year
g = data.groupby(
    ["continent", "year"]
)["lifeExp"].mean().unstack()

print(g)

# Plot bar chart
g.plot(kind="bar", figsize=(10, 5))

plt.title("Average Life Expectancy: 1952 vs 2007")
plt.xlabel("Continent")
plt.ylabel("Average Life Expectancy")
plt.legend(title="Year")
plt.tight_layout()
plt.show()