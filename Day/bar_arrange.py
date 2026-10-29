import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


month = ["Jan", "Feb", "Mar", "Apr"]
jan = [100, 120, 150, 130]
feb = [90, 110, 140, 160]
march = [80, 100, 130, 150]
x = np.arange(len(month))

plt.bar(x - 1, jan, width=0.3, label="January")
plt.bar(x, feb, width=0.3, label="February")
plt.bar(x + 1, march, width=0.3, label="March")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.xticks(x, month)
plt.legend()
plt.tight_layout()
plt.show()
