import pandas as pd
import matplotlib.pyplot as plt

surveys_df = pd.read_csv("surveys.csv")

print()
species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)

species_counts.plot(kind = 'bar')
plt.show()
