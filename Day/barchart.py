import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px 

#create the training dataset 

np.random.seed(42)
df = pd.DataFrame({
    "Month" : [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "North" : [120,135,150,160,175,190,200,210,225,240,255,270],
    "South" : [100,110,125,140,150,165,175,190,205,220,230,250],
    "East"  : [80,95,105,120,135,145,160,175,185,200,215,230],
    "West" : [90,100,115,130,140,155,170,180,195,210,225,245],
    "Marketing_Spend" : [20,25,28,30,32,35,38,40,42,45,48,50],
    "Customers" : [200,240,280,310,350,390,420,460,490,530,570,610],
  
})
regions=["North","South","East","West"]
sales=[120,100,80,90]
plt.figure(figsize=(9,5))
plt.bar(regions,sales,color="steelblue")
plt.title("Regional Sales Comparison")
plt.xlabel("REGIONS")
plt.ylabel("SALES")
plt.grid(axis="y",alpha=0.3)
plt.show()