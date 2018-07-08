import pandas as pd
import numpy as np
import argparse
import math

DEBUG_MODE = False

if(DEBUG_MODE == True):
    # Sets dataset location to development environment paths
    input_filename = 'febrl-data/dedup-dsgen/dataset_A_1000.csv'
    output_filename = 'febrl-data-processed/dedup-dsgen/dataset_A_1000_processed.csv'
else:
    # Read input and output data filenames from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('input_filename',
        help='FEBRL input dataset filename')
    parser.add_argument('output_filename',
        help='Output transformed data for DNN processing')
    parser.add_argument('--file_format', dest='file_format',
        help='CSV or TSV')
    parser.add_argument('--include_header', dest='header',
        help='True/False to include column names in first row')
    parser.add_argument('--fields', dest='fields',
        help='\'name\', \'name_address\', \'all\'')

    args = parser.parse_args()

    input_filename = args.input_filename
    output_filename = args.output_filename
    include_header = (args.header == "True")
    file_format = args.file_format
    fields = args.fields
   

# Use pandas to read input data and manipulate dataset
febrl_data = pd.read_csv(input_filename,
    header=0,
    sep=',')

print('Read {} rows from {}'.format(febrl_data.shape[0], input_filename))

# FEBRL dataset contains the original record in rows with even rec_id
# and duplicate records in rows numbered with odd rec_id
# The dataset includes the blocking number, which we will not use

# Remove blocking number
febrl_data = febrl_data.drop(columns=['blocking_number'])

# Copy even and odd rec_id rows into two data frames
even_rows = pd.DataFrame(data=febrl_data.loc[febrl_data['rec_id'] % 10 == 0])
odd_rows = pd.DataFrame(data=febrl_data.loc[febrl_data['rec_id'] % 10 != 0])
del febrl_data

# Change the index rows that are % 1 to - 1 and column names to *_duplicate

even_rows.rec_id = even_rows.rec_id / 10
odd_rows.rec_id = odd_rows.rec_id / 10
even_rows['rec_id'] = even_rows.rec_id.round(0)
odd_rows['rec_id'] = odd_rows.rec_id.round(0)


odd_rows = odd_rows.rename(index=str, columns={
    'given_name':       'given_name_duplicate',
    'surname':          'surname_duplicate',
    'street_number':    'street_number_duplicate',
    'address_1':        'address_1_duplicate',
    'address_2':        'address_2_duplicate',
    'suburb':           'suburb_duplicate',
    'postcode':         'postcode_duplicate',
    'state':            'state_duplicate',
    'date_of_birth':    'date_of_birth_duplicate',
    'age':              'age_duplicate',
    'phone_number':     'phone_number_duplicate',
    'soc_sec_id':       'soc_sec_id_duplicate'
})

# Join both sets on index (which should be equal by now)
febrl_df = pd.merge(even_rows, odd_rows, on='rec_id').sort_values(by='rec_id')

# Replace all NA fields with empty strings
febrl_df = febrl_df.fillna('')

# Char to use as field separator
field_sep = '_'

# Create fields for output
if fields == 'name':
    febrl_df['original'] = febrl_df.given_name + field_sep + febrl_df.surname
    febrl_df['duplicate'] = febrl_df.given_name_duplicate + field_sep + febrl_df.surname_duplicate
elif fields == 'name_address':
    febrl_df['original'] = febrl_df.given_name + field_sep + febrl_df.surname + field_sep + febrl_df.street_number.astype(str) + field_sep + febrl_df.address_1 + field_sep + febrl_df.address_2 + field_sep + febrl_df.suburb + field_sep + febrl_df.postcode.astype(str) + field_sep + febrl_df.state
    febrl_df['duplicate'] = febrl_df.given_name_duplicate + field_sep + febrl_df.surname_duplicate + field_sep + febrl_df.street_number_duplicate.astype(str) + field_sep + febrl_df.address_1_duplicate + field_sep + febrl_df.address_2_duplicate + field_sep + febrl_df.suburb_duplicate + field_sep + febrl_df.postcode_duplicate.astype(str) + field_sep + febrl_df.state_duplicate
elif fields == 'all':
    febrl_df['original'] = febrl_df.given_name + field_sep + febrl_df.surname + field_sep + febrl_df.street_number + field_sep + febrl_df.address_1 + field_sep + febrl_df.address_2 + field_sep + febrl_df.suburb + field_sep + febrl_df.postcode + field_sep + febrl_df.state + field_sep + febrl_df.date_of_birth + field_sep + febrl_df.age + field_sep + febrl_df.phone_number + field_sep + febrl_df.soc_sec_id
    febrl_df['duplicate'] = febrl_df.given_name_duplicate + field_sep + febrl_df.surname_duplicate + field_sep + febrl_df.street_number_duplicate + field_sep + febrl_df.address_1_duplicate + field_sep + febrl_df.address_2_duplicate + field_sep + febrl_df.suburb_duplicate + field_sep + febrl_df.postcode_duplicate + field_sep + febrl_df.state_duplicate + field_sep + febrl_df.date_of_birth_duplicate + field_sep + febrl_df.age_duplicate + field_sep + febrl_df.phone_number_duplicate + field_sep + febrl_df.soc_sec_id_duplicate

# Add is_duplicate field (always set to 'y')
febrl_df['is_duplicate'] = 'y'
# Remove all other columns
febrl_df = febrl_df.loc[:,febrl_df.columns.intersection(['original', 'duplicate', 'is_duplicate'])]


# Output new dataset
if file_format == 'CSV':
    sep = ','
else:
    sep = '\t'
febrl_df.to_csv(output_filename, index=False, header=include_header,sep=sep)

print('Written {} rows to {}'.format(febrl_df.shape[0], output_filename))

    