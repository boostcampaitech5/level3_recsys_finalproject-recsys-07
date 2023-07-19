import pandas as pd

df = pd.read_csv("../../data/durecdial/dev_sentiment.csv")
# df_user = pd.read_csv("../../data/durecdial/train_user.csv")
# df_log = pd.read_csv("../../data/durecdial/train_log.csv")
max_si = max(df.sentence_index)
size = df.size
columns = df.columns
user_count = len(df.user_id.unique())
