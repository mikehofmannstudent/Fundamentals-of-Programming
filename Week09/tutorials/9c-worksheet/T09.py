import pandas as pd
surveys_df = pd.read_csv("surveys.csv")

print()
print(surveys_df[0:3])

print()
print(surveys_df[:5])
print()
print(surveys_df[-1:])

print()
print(surveys_df.iloc[0:3, 1:4])
print()
print(surveys_df.loc[[0,10], :])
print()
print(surveys_df.loc[0, ['species_id', 'plot_id', 'weight']])
print()
print(surveys_df.loc[[0,10], :])
