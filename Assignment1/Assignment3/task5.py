# Task 5: Bubble chart 
# • Draw an interactive chart where bubble size shows population and colour shows continent: 
# fig = px.scatter(gap_2007, x="gdpPercap", y="lifeExp", size="pop", color="continent", 
# hover_name="country", log_x=True, size_max=50) 
# fig.show() 
# • Which continent has most of the countries with low life expectancy? 
# • Hover over the largest bubbles and write the names of two of them.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

gap = px.data.gapminder()
gap_2007 = gap[gap['year'] == 2007]

# Step-1: Create interactive bubble chart
fig = px.scatter(
    gap_2007,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=50,
    title="GDP vs Life Expectancy(2007)"
)

# Step-2: Update aixs labels
fig.update_layout(
    xaxis_title="GDP per Capita (USD,Log Scale)",
    yaxis_title="Life Expectancy(Year)"
)
fig.show()