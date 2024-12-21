import pandas as pd 
def delete_duplicate(df):
    """
    去除重复值
    """
    df.drop_duplicates(inplace=True)
    return df
def delete_missing(df):
    """
    去除缺失值
    """
    df.dropna(inplace=True)
    return df
def delete_outlier(df):
    """
    去除异常值
    """