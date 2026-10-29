# Task 6: Correlation heatmap 
# • Calculate the correlation matrix of lifeExp, pop and gdpPercap using .corr(). 
# • Draw it with sns.heatmap(..., annot=True, cmap="coolwarm", vmin=-1, vmax=1). 
# • Which pair of columns is most strongly related? Which pair has almost no relationship? 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

gap=px.data.gapminder()
gap_2007=gap[gap["year"]==2007]
gap.head()

data=gap_2007[[
    "lifeExp","pop","gdpPercap"
]]
corr_matrix=data.corr()
print(corr_matrix)

plt.figure(figsize={8,6})

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    fmt=".2f"
) 
plt.title("Correlation Heatmap (2007)")
plt.tight_layout()
plt.show()