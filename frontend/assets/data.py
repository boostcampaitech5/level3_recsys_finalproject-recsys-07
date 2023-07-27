import pandas as pd

# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('all')

df_user = pd.read_csv("../data/durecdial/train_user_small.csv")
df_sentence = pd.read_csv("../data/durecdial/train_sentence_small.csv")
df_sentence_small = pd.read_csv("../data/durecdial/train_sentence_xs.csv")
data_format = pd.read_csv("../data/data_format.csv")
data_format_short = pd.read_csv("../data/data_format_short.csv")
user_format = pd.read_csv("../data/user_format.csv")
model_eval = pd.read_csv("../data/model_metric/model_eval.csv")
model_eval_percent = pd.read_csv("../data/model_metric/model_eval_percent.csv")
max_si = max(df_sentence.sentence_index)
size = df_sentence.size
columns_s = df_sentence.columns
columns_u = df_user.columns
columns = list(df_sentence.columns)
columns.extend(list(df_user.columns))
user_count = len(df_user)

kgsf_raw = [eval(t) for t in open("../data/model_metric/KGSF")]
kbrd_raw = [eval(t) for t in open("../data/model_metric/KBRD")]
insp_raw = [eval(t) for t in open("../data/model_metric/INSPIRED")]
redial_raw = [eval(t) for t in open("../data/model_metric/Redial")]

rec_metric = [
    "hit@1",
    "hit@10",
    "hit@50",
    "mrr@1",
    "mrr@10",
    "mrr@50",
    "ndcg@1",
    "ndcg@10",
    "ndcg@50",
]
gen_metric = [
    "bleu@1",
    "bleu@2",
    "bleu@3",
    "bleu@4",
    "dist@1",
    "dist@2",
    "dist@3",
    "dist@4",
]

redial_result_recommendation = {rm: list() for rm in rec_metric}
redial_result_conversation = {rm: list() for rm in gen_metric}
kgsf_result_recommendation = {rm: list() for rm in rec_metric}
kgsf_result_conversation = {rm: list() for rm in gen_metric}
kbrd_result_recommendation = {rm: list() for rm in rec_metric}
kbrd_result_conversation = {rm: list() for rm in gen_metric}
insp_result_recommendation = {rm: list() for rm in rec_metric}
insp_result_conversation = {rm: list() for rm in gen_metric}

for kgsf in kgsf_raw:
    # recommendation
    if "hit@1" in kgsf:
        for k in kgsf:
            if k in kgsf_result_recommendation:
                kgsf_result_recommendation[k].append(kgsf[k])

    # conversation
    if "bleu@1" in kgsf:
        for k in kgsf:
            if k in kgsf_result_conversation:
                kgsf_result_conversation[k].append(kgsf[k])

for kbrd in kbrd_raw:
    # recommendation
    if "hit@1" in kbrd:
        for k in kbrd:
            if k in kbrd_result_recommendation:
                kbrd_result_recommendation[k].append(kbrd[k])

    # conversation
    if "bleu@1" in kbrd:
        for k in kbrd:
            if k in kbrd_result_conversation:
                kbrd_result_conversation[k].append(kbrd[k])

for insp in insp_raw:
    # recommendation
    if "hit@1" in insp:
        for k in insp:
            if k in insp_result_recommendation:
                insp_result_recommendation[k].append(insp[k])

    # conversation
    if "bleu@1" in insp:
        for k in insp:
            if k in insp_result_conversation:
                insp_result_conversation[k].append(insp[k])


for redial in redial_raw:
    # recommendation
    if "hit@1" in redial:
        for k in redial:
            if k in redial_result_recommendation:
                redial_result_recommendation[k].append(redial[k])

    # conversation
    if "bleu@1" in redial:
        for k in redial:
            if k in redial_result_conversation:
                redial_result_conversation[k].append(redial[k])


def get_model_eval(col):
    return model_eval[model_eval[col] == 1]


def get_model_eval_percent(col):
    return model_eval_percent[model_eval_percent[col] == 1]
