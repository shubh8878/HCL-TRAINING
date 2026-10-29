# Task 7: Pair plot 
# • Draw sns.pairplot(iris, hue="species", vars=["sepal_length", "sepal_width", 
# "petal_length", "petal_width"]). 
# • Which two measurements separate the three species best? Which species is the easiest to 
# identify?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()    # Restaurant bills and tips
iris = px.data.iris()    # Flower measurements
stocks = px.data.stocks() # Weekly stock prices

(tips.head())

sns.pairplot(
    iris,
    hue = "species",
    vars = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
)

plt.show()