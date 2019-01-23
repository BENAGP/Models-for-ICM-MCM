# -*- coding:UTF-8 -*-
import numpy as np 
import pandas as pd 
from datetime import datetime
import matplotlib.pylab as plt

df = pd.read_csv(U'DATA6.csv',encoding='utf-8',index_col='date')
df.index = pd.to_datetime(df.index)
ts = df['y']

print(df)
ts.head()
ts.head().index