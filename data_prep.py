import numpy as np
import pandas as pd

# def fill_missing():
#     pass


# missing data statistics: 
def find_missing(df):
    missing_count = df.isna().sum(axis=0)
    missing_percent = missing_count / len(df) * 100

    missing_data = pd.DataFrame({
        'NaN Count': missing_count,
        'Percentage [%]': missing_percent
    }).sort_values(by='NaN Count', ascending=False)
    missing_data.index.name = 'Column Name'

    missing_data = missing_data[missing_data['NaN Count'] > 0]
    print(missing_data)
    return

def have_uniformed(df):
    uniformed_columns = []
    for i in df.columns:
        unique_values = df[i].dropna().unique()
        
        if len(unique_values) == 1:
            uniformed_columns.append(i)
            
    if uniformed_columns:
        for i in uniformed_columns:
            print("\nThe DataFrame contains columns with uniformed values:", i)  
        return True
    else:
        print("\nThe DataFrame does not contain columns with uniformed values.")
        return False
    
def have_duplicate(df):
    duplicated_data = df.duplicated()
    num_duplicated_data = df.duplicated().sum()
    if duplicated_data.any():
        print(f"\nNumber of duplicated records: {num_duplicated_data}")
        return True
    else:
        print("\nThe DataFrame does not contain any dupplicated records.")
        return False
    
def data_faults(df):
    find_missing(df)
    have_uniformed(df)
    have_duplicate(df)
    return

def unique_values(df):
    # Get categorical variable columns unique values series
    unique_sorted_df = pd.concat( [df[col].drop_duplicates().sort_values().reset_index(drop=True) 
                                   for col in df] , axis = 1
                                )
    print(unique_sorted_df)
    return unique_sorted_df

def replace_ordinals(df, value_list):
    # Replace string data with their index value in the "string_value_list" variable
    for col, uni_val in value_list.items():
        map_dict = {k: v for v, k in enumerate(uni_val)}
        df[col]= df[col].map(map_dict)
    #-----------------------------------------------------------