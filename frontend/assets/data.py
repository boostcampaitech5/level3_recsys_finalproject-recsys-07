import pandas as pd

# df = pd.read_csv("../data/durecdial/dev_sentiment.csv")
df_user = pd.read_csv("../data/durecdial/train_user_xs.csv")
df_sentence = pd.read_csv("../data/durecdial/train_sentence_xs.csv")
model_eval = pd.read_csv("../data/model_metric/model_eval.csv")
max_si = max(df_sentence.sentence_index)
size = df_sentence.size
columns_s = df_sentence.columns
columns_u = df_user.columns
columns = list(df_sentence.columns)
columns.extend(list(df_user.columns))
user_count = len(df_user)
