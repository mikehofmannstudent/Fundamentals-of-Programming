import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

budget = pd.read_csv('budget.csv')
budget = budget.sort_values(by='Budget', ascending=False)[:10]
sns.set_style('darkgrid')

bar_plot = sns.barplot(x=budget['Department'], y=budget['Budget'],
                       palette='muted', order=budget['Department'].tolist())

plt.xticks(rotation=90)
plt.show()
