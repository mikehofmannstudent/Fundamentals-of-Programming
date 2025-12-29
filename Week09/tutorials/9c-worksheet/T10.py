import pandas as pd
surveys_df = pd.read_csv("surveys.csv")

print()
print(surveys_df[surveys_df.year == 2002])
print()
print(surveys_df[surveys_df.year != 2002])
print()
print(surveys_df[(surveys_df.year >= 1980) & (surveys_df.year <= 1985)])
