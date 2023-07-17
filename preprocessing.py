import json, pandas as pd
import numpy as np

dev = pd.read_csv('../data/dev.csv')
train = pd.read_csv('../data/train.csv')
test = pd.read_csv('../data/test.csv')

def pp(df, length):
    df['conversation'] = df.conversation.apply(lambda x:pd.Series(x.replace("',", '",')))
    temp_sentence = df.conversation.apply(lambda x:pd.Series(x.split('",')))
    temp_goal_topic = df.goal_topic_list.apply(lambda x:pd.Series(x.split(',')))
    temp_goal_type = df.goal_type_list.apply(lambda x:pd.Series(x.split(',')))
    temp_knowledge = df.knowledge.apply(lambda x:pd.Series(x.split(']')))
    
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
    
    for i in range(length): # 5678 811
        for j in range(len(temp_sentence['sentence'][i])):
            temp_sentence['sentence'][i][j] = temp_sentence['sentence'][i][j].strip()
            temp_sentence['sentence'][i][j] = temp_sentence['sentence'][i][j].strip("'")
    
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

    # recdial: 추천 대화 여부(1: 추천 관련 대화, 0: 추천 관련 없는 대화)
    df['recdial'] = np.where(df['goal_type'].str.contains('recommendation'), 1, 0)

    return df

train = pp(train, 5678)
# test = pp(test)
dev = pp(dev, 811)

train.to_csv('../data/train_data.csv',index=False)
# test.to_csv('../data/test_data.csv',index=False)
dev.to_csv('../data/dev_data.csv',index=False)
