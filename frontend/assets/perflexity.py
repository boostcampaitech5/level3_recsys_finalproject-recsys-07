import os
import nltk
import re
from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
from assets.data import df_sentence

# perflexity
if os.path.exists("./assets/perflexity.txt"):
    print("Load perflexity File...")

    d_pp = []
    with open("./assets/perflexity.txt", "r") as file:
        for i in file:
            d_pp.append(float(i.strip()))
    print("Done.")

else:
    print("calculating perflexity...")
    # 각 instance 별로 문장들을 어레이에 넣는다
    dialogues = df_sentence.groupby("user_id")
    stop_words = list(get_stop_words("en"))  # About 900 stopwords
    nltk_words = list(stopwords.words("english"))  # About 150 stopwords
    stop_words.extend(nltk_words)
    d_pp = []  # 각 dialogue의 평균 문장 perplexity를 모아놓은 array
    for key, item in dialogues:
        # per dialogue
        # 각 어레이(instance) 별로 perplexity를 계산한다.
        # 문장 별 perplexity 계산의 평균으로 구한다.
        # 계산 방법
        # https://medium.com/nlplanet/two-minutes-nlp-perplexity-explained-with-simple-probabilities-6cdc46884584
        s_group = dialogues.get_group(key)["sentence"]
        s_group_2 = []
        for s in s_group:
            word_list = re.findall(r"\w+", s, flags=re.UNICODE)
            filtered_words = [
                word for word in word_list if word not in stopwords.words("english")
            ]
            output = " ".join([w for w in filtered_words if w not in stop_words])
            s_group_2.append(output)
        tokenized_text = [
            list(map(str.lower, nltk.tokenize.word_tokenize(sent)))
            for sent in s_group_2
        ]

        n = 2
        train_data, padded_vocab = padded_everygram_pipeline(n, tokenized_text)
        model = MLE(n)
        model.fit(train_data, padded_vocab)
        test_data, _ = padded_everygram_pipeline(n, tokenized_text)
        pp_list = []
        for i, test in enumerate(test_data):
            pp = model.perplexity(test)
            # print("PP({0}):{1}".format(tokenized_text[i], pp))
            pp_list.append(pp)
        avg_pp_dialogue = sum(pp_list) / len(pp_list)
        d_pp.append(avg_pp_dialogue)
        file_name = "./assets/perflexity.txt"
    with open(file_name, "w+") as file:
        file.write("\n".join(list(map(str, d_pp))))
    print("Done.")
