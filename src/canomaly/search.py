'''
Search for cumulative changes 
'''

import pandas as pd

def cummax():
    ...

def cummin():
    ...

def cum_abs_min():
    ...

def cum_abs_max():
    ...

# TODO: Handle repeat dates
# TODO: Support arbitrary aggregation function

def doubly_aggregate(df, agg_f, column, group):
    """
    Applies a double aggregation to a column in a dataframe based on a grouping variable.

    Parameters:
    -----------
    df : pandas.DataFrame
        A pandas DataFrame with columns matching the arguments `column` and `group`.
    agg_f : function
        An aggregation function to be applied to the `column` within each group.
    column : str
        The name of the column to be aggregated.
    group : str
        The name of the grouping variable.

    Returns:
    --------
    pandas.DataFrame
        A DataFrame containing the doubly-aggregated column paired with the group.
    """
    # First aggregation
    agg_column = df.groupby(group)[column].agg(agg_f)
    # Sort by group
    agg_column_sorted = agg_column.sort_index()
    # Apply the aggregation function again cumulatively
    doubly_agg_column = pd.Series(index=agg_column_sorted.index, dtype=df.column.dtype)
    for i, (group_name, group_value) in enumerate(agg_column_sorted.items()):
        doubly_agg_column[group_name] = agg_f(agg_column_sorted.iloc[:i+1])
    return doubly_agg_column

