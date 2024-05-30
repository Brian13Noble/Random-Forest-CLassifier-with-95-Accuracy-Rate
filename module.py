def map_strings_to_integers(df):
    """
    Maps string values in a DataFrame to integers.
    
    Parameters:
        df (DataFrame): Input DataFrame with string values.
        
    Returns:
        DataFrame: DataFrame with string values mapped to integers.
    """
    df_mapped = df.copy()
    
    for column in df_mapped.columns:
        if df_mapped[column].dtype == 'object':
            unique_values = df_mapped[column].unique()
            mapping = {value: index for index, value in enumerate(unique_values)}
            df_mapped[column] = df_mapped[column].map(mapping)
    
    return df_mapped

