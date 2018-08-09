import pandas as pd
#import keras
from sklearn.model_selection import train_test_split

febrl_data_filename = 'febrl-data-processed/dedup-dsgen/dataset_A_1000_processed.csv'

# Read pre-processed febrl data and remove null/empty fields
febrl_df = pd.read_csv(febrl_data_filename)
febrl_df = febrl_df.fillna('')

# First we will train a network that will compare names

# Create name field based on first and last name fields
febrl_df['name'] = febrl_df.given_name + ' ' + febrl_df.surname
febrl_df['name_duplicate'] = febrl_df.given_name_duplicate + ' ' + febrl_df.surname_duplicate

# Remove all other columns
febrl_df = febrl_df.loc[:,febrl_df.columns.intersection(['name', 'name_duplicate'])]

name_max_length = febrl_df.name.str.len().max()
name_duplicate_max_length = febrl_df.name_duplicate.str.len().max()

input_max_len = name_max_length if name_max_length > name_duplicate_max_length else name_duplicate_max_length

print(input_max_len)

# Split data into train and test
train, test = train_test_split(febrl_df, test_size=0.2)




