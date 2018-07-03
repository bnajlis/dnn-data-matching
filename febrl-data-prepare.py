import pandas as pd
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

    args = parser.parse_args()

    input_filename = args.input_filename
    output_filename = args.output_filename

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
febrl_data_duplicates = pd.merge(even_rows, odd_rows, on='rec_id')

# Output new dataset
febrl_data_duplicates.sort_values(by='rec_id').to_csv(output_filename, index=False)

print('Written {} rows to {}'.format(febrl_data_duplicates.shape[0], output_filename))