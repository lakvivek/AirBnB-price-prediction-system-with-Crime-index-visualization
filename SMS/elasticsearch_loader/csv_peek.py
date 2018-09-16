import pandas as pd

csvfile = "../data/processed_NYPD.csv"

df = pd.read_csv(csvfile)
print(df.shape)