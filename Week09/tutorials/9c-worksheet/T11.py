import pandas as pd
surveys_df = pd.read_csv("surveys.csv")

print()
true_copy_surveys_df = surveys_df.copy()

ref_surveys_df = surveys_df
