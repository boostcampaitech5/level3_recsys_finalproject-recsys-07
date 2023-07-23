import nltk
import re
import os
from nltk.corpus import stopwords
from nltk.util import ngrams
from stop_words import get_stop_words
from assets.data import df_sentence


def distinct_n_s_level(sentence, n):
    if len(sentence) == 0:
        return 0.0
    word_list = re.findall(r"\w+", i, flags=re.UNICODE)
    filtered_words = [
        word for word in word_list if word not in stopwords.words("english")
    ]
    output = " ".join([w for w in filtered_words if w not in stop_words])
    NGRAMS = ngrams(nltk.word_tokenize(output), 1)
    D_NGRAMS = set(NGRAMS)
    s_dngram = len(D_NGRAMS) / len(word_list)
    return s_dngram


if os.path.exists("./assets/ngram.txt"):
    print("Load N-gram File...")
    d_array = []
    with open("./assets/ngram.txt", "r") as file:
        for i in file:
            d_array.append(float(i.strip()))
    print("Done.")

else:
    print("Calculate N-gram...")

    # 각 instance 별로 문장들을 어레이에 넣는다
    dialogues = df_sentence.groupby("user_id")
    stop_words = list(get_stop_words("en"))  # About 900 stopwords
    nltk_words = list(stopwords.words("english"))  # About 150 stopwords
    stop_words.extend(nltk_words)

    d_array = []  # 1. 각 대화 별 s_dngram 평균을 저장한다. length = # of dialogues
    ss_array = []
    for key, item in dialogues:
        # per dialogue
        # 각 어레이(instance) 별로 sentence level distinct n-gram을 계산한다.
        # 계산 방법 : https://github.com/neural-dialogue-metrics/Distinct-N/blob/main/distinct_n/metrics.py#L3
        s_group = dialogues.get_group(key)["sentence"]
        s_word_len = []
        # s-level dngram 저장하는 array
        s_array = []
        for i in s_group:
            s_array.append(distinct_n_s_level(i, 1))
        # dialogue-level distinct ngram : average distinct-N of a list of sentences (the dialogue)
        ss_array.append(s_array)
        d_dngram = sum(s_array) / len(s_group)
        d_array.append(d_dngram)
    avg_dataset = sum(d_array) / len(d_array)  # 2. 전체 데이터셋의 d_dngram 평균값. type = float
    file_name = "./assets/ngram.txt"
    with open(file_name, "w+") as file:
        file.write("\n".join(list(map(str, d_array))))

    print("Done.")
