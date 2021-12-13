##################
#POTENTIAL CUSTOMER REVENUE BY RULE-BASED CLASSIFICATION
##################


import pandas as pd
pd.pandas.set_option('display.max_columns', None)

def load_persona():
    df = pd.read_csv('Bootcamp/Week2/Ders Oncesi Notlar/persona.csv')
    return df
df = load_persona()

def check_df(dataframe, head=5):
    print("############SHAPE##############")
    print(dataframe.shape)
    print("############TYPES#############")
    print(dataframe.dtypes)
    print("############HEAD##############")
    print(dataframe.head(head))
    print("############TAIL##############")
    print(dataframe.tail(head))
    print("#############NA###############")
    print(dataframe.isnull().sum())
    print("##########QUANTILES###########")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)


df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})


agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)


agg_df = agg_df.reset_index()


agg_df["AGE"].max()
agg_df["AGE"].min()


agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins = [14, 20, 28, 38, 48, 58, 66], labels = ["14_20", "20_28", "28_38", "38_48", "48_58", "58_66"])



agg_df["costumers_level_based"] = [(col[0]+"_"+col[1]+"_"+col[2]+"_"+col[5]).upper() for col in agg_df.values]

agg_df = agg_df[["costumers_level_based","PRICE"]]

agg_df = agg_df.groupby("costumers_level_based").agg({"PRICE": "mean"}).round(2)

agg_df = agg_df.reset_index()


agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels = ["D", "C", "B", "A"])


new_user = "USA_ANDROID_MALE_28_38"
agg_df[agg_df["costumers_level_based"] == new_user]

