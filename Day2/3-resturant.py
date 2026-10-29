import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()
print(tips.head())

categories = ["Electronic", "Clothing", "Grocery", "Furniture", "Sports"]
sales = [45000, 30000, 20000, 15000, 10000]

plt.figure(figsize=(7, 7))

plt.pie(sales, labels=categories, autopct="%1.2f%%")

plt.title("Sales Analysis")

plt.show()