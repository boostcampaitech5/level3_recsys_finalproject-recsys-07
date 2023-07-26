import json, pandas as pd
import numpy as np

# DuRecDial 2.0 데이터셋을 DASHMON에 업로드 할 수 있는 포맷으로 전처리 하는 코드
print("Data Preprocessing Start ...")

# 파일 open
train = pd.DataFrame()
with open('./data/en_train.txt','r') as f: # 원본 파일 경로
    while True:
        line = f.readline()
        if not line:
            break
        js = json.loads(line)
        low = pd.json_normalize(js)
        train = pd.concat([train,low])

# column명 처리
columns = list(train.columns)
for i in range(len(columns)):
    columns[i] = columns[i].replace('.','_')
    columns[i] = columns[i].replace(' ','_')
    columns[i] = columns[i].lower()
train.columns = columns

# 중간 csv 파일 저장 / 불러오기
# train = pd.read_csv('./data/train.csv')
# train = pd.read_csv('../data/train.csv')

print("JSON to CSV Finish ...")
print("Sentence Separation Start ...")

def pp(df, length):
    # 여러 값을 포함하는 feature의 값들을 여러 행으로 분리하기
    # 각 feature의 List들을 열로 바꿔줌으로써 Feature별 dataframe이 생성됨
    df['conversation'] = df.conversation.apply(lambda x:pd.Series(x.replace("',", '",')))
    temp_sentence = df.conversation.apply(lambda x:pd.Series(x.split('",')))
    temp_goal_topic = df.goal_topic_list.apply(lambda x:pd.Series(x.split(',')))
    temp_goal_type = df.goal_type_list.apply(lambda x:pd.Series(x.split(',')))
    temp_knowledge = df.knowledge.apply(lambda x:pd.Series(x.split(']')))
    
    # 각 feature에서 탄생한 dataframe을 stack을 통해 다시 단일 열로 만들어주기
    # 이제 index level을 가짐
    temp_sentence = temp_sentence.stack().to_frame('sentence')
    temp_goal_topic = temp_goal_topic.stack().to_frame('goal_topic')
    temp_goal_type = temp_goal_type.stack().to_frame('goal_type')
    temp_knowledge = temp_knowledge.stack().to_frame('knowledge')

    temp_sentence.sentence = temp_sentence.sentence.str.replace(r"\[.*\]","")
    temp_sentence.sentence = temp_sentence.sentence.str.replace(r"\]","")
    temp_sentence.sentence = temp_sentence.sentence.str.replace(r"\" ","")
    temp_sentence.sentence = temp_sentence.sentence.str.replace(r"\"","")
    temp_sentence.sentence = temp_sentence.sentence.str.strip("'")
    temp_knowledge.knowledge = temp_knowledge.knowledge.str.replace(r"\'","")
    temp_knowledge.knowledge = temp_knowledge.knowledge.str.strip()
    temp_knowledge.knowledge = temp_knowledge.knowledge.str.strip(',')
    
    # sentence 시작, 끝에 ' 기호 있으면 제거
    for i in range(length): # train: 5678, dev: 811 // length: 데이터의 행의 길이
        for j in range(len(temp_sentence['sentence'][i])):
            temp_sentence['sentence'][i][j] = temp_sentence['sentence'][i][j].strip()
            temp_sentence['sentence'][i][j] = temp_sentence['sentence'][i][j].strip("'")
    
    # sentence 기준으로 feature 묶어주기
    output = pd.concat([temp_sentence,temp_goal_topic,temp_goal_type,temp_knowledge],axis=1)
    output = output.reset_index(level=1)
    output = output.rename(columns={'level_1':'sentence_index'})
    
    output.iloc[:,1:] = output.iloc[:,1:].apply(lambda x:x.str.replace(r"\"",""))
    output.iloc[:,1:] = output.iloc[:,1:].apply(lambda x:x.str.replace(r"\[",""))
    output.iloc[:,1:] = output.iloc[:,1:].apply(lambda x:x.str.replace(r"\]",""))
    output.iloc[:,1:] = output.iloc[:,1:].apply(lambda x:x.str.strip())
    output.iloc[:,1:] = output.iloc[:,1:].apply(lambda x:x.str.strip("'"))
    output = output.replace('',np.nan)
    
    df.drop(columns=['goal','conversation','goal_topic_list','goal_type_list','knowledge'],inplace=True)
    
    # situation 변수를 time, place, date, topic, wday 변수로 분리
    temp_situation = df.situation.apply(lambda x:pd.Series(x.split(',')))
    temp_situation.columns = ['time','overview']
    temp_situation.time = temp_situation.time.str.replace("Time: ","")
    
    temp_situation['date'] = temp_situation['time'].str.extract('(\d* \d* - \d* - \d*)')
    temp_situation['time'] = temp_situation['time'].str.extract('(\d*:\d)')
    temp_situation['topic'] = temp_situation['overview'].str.extract('Topic: (.*)')
    temp_situation = temp_situation.apply(lambda x:x.str.replace(r' Topic: .*',''))
    wday = temp_situation['overview'].str.extract('( \w*day)')
    temp_situation = temp_situation.apply(lambda x:x.str.replace(r' \w*day',''))
    temp_situation['wday'] = wday
    temp_situation = temp_situation.apply(lambda x:x.str.strip())
    temp_situation = temp_situation.rename(columns={'overview':'place'})
    temp_situation.date = temp_situation.date.str.replace(' ','')

    df = pd.concat([df,temp_situation],axis=1)
    df.drop(columns=['situation'],inplace=True)
    df.reset_index(inplace=True)
    df = df.merge(output,left_index=True, right_index=True, how='left')

    return df

train = pp(train, 5678)

print("Data Preprocessing Finish ...")
print("Save CSV File Start ...")

train.to_csv('../data/train_data.csv',index=False) # 파일 저장 위치 경로
print("All Process is Finish ...")
