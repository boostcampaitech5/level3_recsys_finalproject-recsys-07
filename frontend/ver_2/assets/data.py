import pandas as pd

df = pd.read_csv("../../data/durecdial/dev_data_pp.csv")
max_si = max(df.sentence_index)
size = df.size
columns = df.columns
user_count = len(df.user_id.unique())