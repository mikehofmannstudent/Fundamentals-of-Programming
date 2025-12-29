import pandas as pd
surveys_df = pd.read_csv("surveys.csv")
print(surveys_df)

sorted_data = surveys_df.groupby('sex')
print(sorted_data)
print()
print(sorted_data.describe())
print()
print(sorted_data.mean())
