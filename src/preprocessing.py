import pandas as pd

# Explore Dataset

def dataset_info(df):
    print("\n-----First 5 rows------")
    print(df.head())
    
    print("\n-----Last 5 rows----")
    print(df.tail())
    
    print("\n----Dataset Info----")
    print(df.info())
    
    print("\n----Dataset Shape----")
    print(df.shape)
    
    print("\n----Columns----")
    print(df.columns)
    
    print("\n----Data types----")
    print(df.dtypes)
    
    print("\n-----stastical summery-----")
    print(df.describe())
    
def check_missing_values(df):
    print("\n-----Check Missing Values-----")
    print(df.isnull().sum())
    
def check_duplicates(df):
    print("\n-----Duplicate Records-----")
    print(df.duplicated().sum())
    
def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

def clean_name_col(df):
    df["Name"] = df["Name"].str.title()
    return df

def save_clean_data(df):
    df.to_csv("data/healthcare_cleaned.csv",index = False)
    print("\nCleaned dataset saved successfully")
