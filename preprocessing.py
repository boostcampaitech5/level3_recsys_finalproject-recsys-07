import pandas as pd

dev = pd.read_csv("./data/dev.csv")
train = pd.read_csv("./data/train.csv")
test = pd.read_csv("./data/test.csv")


def pp(df):
    temp_sentence = df.conversation.apply(lambda x: pd.Series(x.split(",")))
    temp_goal_topic = df.goal_topic_list.apply(lambda x: pd.Series(x.split(",")))
    temp_goal_type = df.goal_type_list.apply(lambda x: pd.Series(x.split(",")))
    temp_knowledge = df.knowledge.apply(lambda x: pd.Series(x.split("]")))
    temp_sentence = temp_sentence.stack().to_frame("sentence")
    temp_goal_topic = temp_goal_topic.stack().to_frame("goal_topic")
    temp_goal_type = temp_goal_type.stack().to_frame("goal_type")
    temp_knowledge = temp_knowledge.stack().to_frame("knowledge")
    output = pd.concat(
        [temp_sentence, temp_goal_topic, temp_goal_type, temp_knowledge], axis=1
    )
    output = output.reset_index(level=1, drop=True)
    df.drop(
        columns=[
            "goal",
            "conversation",
            "goal_topic_list",
            "goal_type_list",
            "knowledge",
        ],
        inplace=True,
    )
    df = df.merge(output, left_index=True, right_index=True, how="left")
    return df


train = pp(train)
test = pp(test)
dev = pp(dev)
train.to_csv("./data/train_pp.csv")
test.to_csv("./data/test_pp.csv")
dev.to_csv("./data/dev_pp.csv")
