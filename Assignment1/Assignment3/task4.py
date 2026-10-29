# Task 4: Linear scale versus log scale
# 	•	Using gap_2007, draw two scatter plots side by side with gdpPercap on the x-axis and lifeExp on the y-axis.
# 	•	Keep the left chart as it is. On the right chart, add set_xscale("log").
# 	•	Which chart is easier to read, and why?
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Gapminder dataset
gap = px.data.gapminder()

gap_2007 = gap[gap["year"] == 2007]


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

gap = px.data.gapminder()
gap_2007 = gap[gap['year'] == 2007]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.scatterplot(data=gap_2007, x="gdpPercap", y="lifeExp", ax=axes[0], color="blue")
axes[0].set_title("Linear Scale (2007)")
axes[0].set_xlabel("GDP per Capita")
axes[0].set_ylabel("Life Expectancy")

sns.scatterplot(data=gap_2007, x="gdpPercap", y="lifeExp", ax=axes[1], color="green")
axes[1].set_xscale("log")
axes[1].set_title("Logarithmic Scale (2007)")
axes[1].set_xlabel("GDP per Capita (Log Scale)")
axes[1].set_ylabel("Life Expectancy")

plt.tight_layout()
plt.show()