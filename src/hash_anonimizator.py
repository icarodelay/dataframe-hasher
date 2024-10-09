import pandas as pd
from hashlib import sha256

def hash_anonimizator(df:pd.DataFrame, column_name:str):
    '''
    Returns the SHA256-hashed string of the original DataFrame column(s).

    Parameters:
        df (pd.DataFrame):The dataframe with the column(s) to hash.
        column_name (str):The string specifying which column(s) from the DataFrame to hash.

    Returns:
        hash_anonimizator(df, column_name):The DataFrame which got some columns SHA256-hashed.   
    '''

    df[column_name] = df[column_name].apply(lambda element: sha256(element.encode('utf-8')).hexdigest())

    return df