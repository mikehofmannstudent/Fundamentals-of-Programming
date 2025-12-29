import pandas as pd
surveys_df = pd.read_csv("surveys.csv")

print()
species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)

print()
do_df = surveys_df.groupby('species_id')['record_id'].count()['DO']
print(do_df)

print()
print(surveys_df['weight'] * 2.2)
