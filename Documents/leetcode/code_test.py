import numpy as np
import pandas as pd


class test:
    def__init__(self,data_path):
        self.data_path = pd.read_csv(data_path, header=0, index_col=None)

    def res(self, res):
        print(res)
