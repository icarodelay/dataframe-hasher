import pandas as pd
from dataframe_hasher import dataframe_hasher

df = pd.read_csv('./data/cadunico.csv', sep=';', encoding='latin-1')
df = dataframe_hasher(df, 'CPF')