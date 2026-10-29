# Task 11: Copy this table into a Markdown cell and complete it based on what you experienced.   
# Then write 2 to 3 lines: which library would you choose for a chart in a lab report, and which for a chart 
# on a web page? Give a reason for each.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = px.data.tips()    # Restaurant bills and tips
iris = px.data.iris()    # Flower measurements
stocks = px.data.stocks() # Weekly stock prices

(tips.head())

comparison_data = {
    "Library": ["Matplotlib", "Seaborn", "Plotly"],
    "Ease of use (easy / medium / hard)": ["Medium", "Easy", "Medium"],
    "Interactive charts? (yes / no)": ["No", "No", "Yes"],
    "Best used for": [
        "Fine-grained customization & static plots", 
        "Statistical data visualization", 
        "Interactive dashboards & web apps"
    ]
}

comparison_df = pd.DataFrame(comparison_data)

print("\n--- Task 11: Library Comparison Table ---")
print(comparison_df.to_string(index=False))