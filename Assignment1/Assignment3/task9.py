# Task 9: Fix a poor chart
# Run this code. It shows the life expectancy of the top 8 European countries, but the chart is badly designed.
# bad = gap_2007[gap_2007["continent"] == "Europe"].nlargest(8, "lifeExp")plt.figure(figsize=(6, 4))plt.bar(bad["country"], bad["lifeExp"],        color=["red", "green", "blue", "yellow", "pink", "orange", "purple", "black"])plt.ylim(79, 82)plt.show()
# 	•	List at least four problems with this chart.
# 	•	Redraw it properly: one colour, a y-axis (or x-axis) that starts at 0, readable country names, a title and axis labels.
# 	•	Write one line on how the bars look different after your fix.