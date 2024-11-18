import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path: str,iscsv: bool=True) -> pd.DataFrame:
    try:
        if iscsv:
            data = pd.read_csv(file_path)
        else:
            data = pd.read_json(file_path)
        return data
    except FileNotFoundError:
        print("File not found")
        return None
    except pd.errors.ParserError:
        print("Invalid file format")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    file_path = r"week8\data.csv"
    file_path_json = r"week8\data.json"
    df = load_data(file_path_json,False)
    if df is not None:
        print(df)
        # print(df.to_string())
        # print(df.head())
        # print(df.tail(10))
        # print(df.info())
        # print(df.describe())
        # print(df.columns)
        # print(df.shape)
        # print(df.isnull().sum())
        # print(df.duplicated().sum())
        # print(df.nunique())
        # print(df.corr())
        # print(df.groupby("Pulse").agg({"Pulse": "count"}))
        # print(df.groupby("Duration").agg({"Duration": ["mean", "std"]}))
        # print(df.pivot_table(index="Duration", columns="Maxpulse", values="Calories", aggfunc="count"))
        # df.plot()
        # df.plot(kind="scatter",x="Duration",y="Calories")
        # df.plot(x="Duration",y="Calories")
        # df.boxplot()
        # df.hist()
        # df.hist(column="Duration")
        # df.hist(column="Calories", bins=20)
        # df.hist(column="Duration", by="Maxpulse")
        # df.hist(column="Calories", by="Maxpulse", bins=20)
        # df.hist(column="Duration", by="Maxpulse", bins=20, figsize=(10, 5))
        # df.hist(column="Calories", by="Maxpulse", bins=20, figsize=(10, 5), cumulative=True)
        # df.hist(column="Duration", by="Maxpulse", bins=20, figsize=(10, 5), density=True)
        # df.hist(column="Duration", by="Maxpulse", bins=20, figsize=(10, 5), cumulative=True, density=True)
        plt.show()