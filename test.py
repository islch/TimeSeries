import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)


dates = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df.loc['all'] = df.apply(lambda x: x.sum(), axis=1)
print(df)
'''

data = pd.read_csv('./data/AirPassengers.csv')
print(data.head())
