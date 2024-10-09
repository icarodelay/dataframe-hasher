import pandas as pd
from hash_anonimizator import hash_anonimizator

df = pd.read_csv('./data/cadunico.csv', sep=';', encoding='latin-1')
df = hash_anonimizator(df, 'CPF')