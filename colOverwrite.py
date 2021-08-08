# Function to overwrite one or more columns of a data frame based on one or more columns from the lookup dataframe
#
# We need the base and lookup dataframes as input, the column names in the base dataframe to be overwritten on,
# Import required packages
#
import pandas as pd


# the column names of the lookup dataframe to be compared with columns of the base dataframe
# Here df_test dataframes are the base
#
# Output is a dataframe with the required columns overwritten
#
# This might not work for just one column to overwrite. Single column overwrite based on a single lookup column needs to be tested
#
# Sample of important arguments:
# columns_to_lookup_base = ['CURRENT_CREDITOR_ID', 'PRE_CHARGEOFF_FLAG']
# columns_to_override_base = ['TERM', 'SETTLEMENT_RATE']
# columns_to_lookup_criteria = ['creditor_current_id', 'pre_chargeoff']
# columns_to_override_lookup = ['term_p90', 'sr_p10']
def multiColOverwrite(
    df_test1,
    df_lookup,
    columns_to_lookup_base,
    columns_to_override_base,
    columns_to_override_lookup,
    columns_to_lookup_criteria,
):

    df_test1.index = pd.MultiIndex.from_arrays(
        [df_test1[col] for col in columns_to_lookup_base]
    )
    df_lookup.index = pd.MultiIndex.from_arrays(
        [df_lookup[col] for col in columns_to_lookup_criteria]
    )
    indexes = df_test1[df_test1.index.isin(df_lookup.index) == True].index

    for i in indexes:
        for j in range(len(columns_to_override_base)):
            df_test1[columns_to_override_base[j]].loc[i] = df_lookup[
                columns_to_override_lookup[j]
            ].loc[i]

    df_test1.index = range(len(df_test1[:, 0]))
    df_test2 = df_test1.copy()
    return df_test2


# Function for single column overwrite
#
# Sample of important arguments
# columns_to_lookup_base = ['CURRENT_CREDITOR_ID']
# columns_to_override_base = ['TERM', 'SETTLEMENT_RATE']
# columns_to_lookup_criteria = ['creditor_current_id']
# columns_to_override_lookup = ['term_p90', 'sr_p10']
def singleColOverwrite(
    df_test,
    df_lookup,
    columns_to_lookup_base,
    columns_to_override_base,
    columns_to_override_lookup,
    columns_to_lookup_criteria,
):
    for index in range(len(columns_to_lookup_base)):
        indexes = df_test[
            df_test[columns_to_lookup_base].isin(
                [df_lookup[columns_to_lookup_criteria].iloc[index]]
            )
            == True
        ].index
        for j in range(len(columns_to_override_base)):
            df_test.loc[indexes, columns_to_override_base[j]] = df_lookup[
                columns_to_override_lookup[j]
            ].iloc[index]
    return df_test


# Testing
print("Hello")
