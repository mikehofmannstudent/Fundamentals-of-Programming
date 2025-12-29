import pandas as pd
import matplotlib.pyplot as plt

budget = pd.read_csv('budget.csv')
plt.style.use = 'default'
budget.index = budget['Department']
print(budget)
budget_plot = budget.plot(kind='bar', title="MN Capital Budget - 2014", legend=False)
fig = budget_plot.get_figure()
fig.savefig("2014-mn-capital-budget.png")
