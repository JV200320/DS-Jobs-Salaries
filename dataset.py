from typing import Union
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class Dataset():

    def __init__(self) -> None:
        url = 'url to repo csv'
        self._df = pd.read_csv(url)
        self.field = None
        self.filter = None

    def filter_by(self, field: str, filter: str, inplace: bool = False) -> Union[pd.DataFrame, None]:
        filtered_data = self._df[self._df[field] == filter]
        if inplace:
            self._df = filtered_data
            return None
        return filtered_data

    def group_by(self, df: pd.DataFrame = None, by: str = None, groupby_method: str = None):
        if df.empty:
            df = self._df
        if not groupby_method:
            groupby_method = 'mean'

        grouped = df.groupby(by)
        grouped_method = getattr(grouped, groupby_method)
        result_df = grouped_method().round(2)

        return result_df

    def persist_answers(self, df: pd.DataFrame):
        reseted_index = df.reset_index()

        reseted_index.to_csv('./answers/answer.csv', index=False)
        reseted_index.to_json('./answers/answer.json', orient='split')

    def create_graph(self, filtered_data, orientation, x, y, xlabel, ylabel):
        if not orientation:
            orientation = 'h'

        fig, ax = plt.subplots(figsize=(12, 12))
        sns.boxplot(data=filtered_data, x=x,
                    y=y, ax=ax, orient=orientation)
        if ylabel:
            ax.set_ylabel(ylabel)
        if xlabel:
            ax.set_xlabel(xlabel)
        fig.savefig('./answers/fig.jpeg')
