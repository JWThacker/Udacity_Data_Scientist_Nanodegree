import pandas as pd


def clean_airbnb_listings(df, **features_dict):
    '''clean airbnb dataset.
    
       params:
           df - a Pandas.DataFrame
           features_dict - a dictionary mapping names of dictionaries to
                           lists of variable names
       returns:
           null - this is an inplace function
    '''
    # change primitive of 'id' from an integer to a string/object
    df['id'] = df['id'].astype('object')
    
    # assign three variables the lists associated with the keys below
    # for better readability.
    features_to_drop = features_dict['features_to_drop']
    features_w_nas_to_drop = features_dict['features_w_nas_to_drop']
    missing_features = features_dict['missing_features']
    
    # merge features_to_drop and features_w_nas_to_drop
    features_to_drop.extend(features_w_nas_to_drop)
    
    # make a list of the features (columns) to drop and then drop them from
    # the dataset
    features_to_drop = [feature for feature in features_to_drop if feature not in missing_features]
    df.drop(columns=features_to_drop, inplace=True)
    
    # replace the % sign in the variables that represent a rate
    for feature in features_dict['rate_features']:
        df[feature] = df[feature].str.replace(r'%', '', regex=True)
        df[feature] = df[feature].astype('double')
    
    # map the 't' and 'f' to their respective boolean values
    for feature in features_dict['features_to_fix']:
        df[feature] = df[feature].replace({'t':True, 'f':False}).astype('bool')
     
    # give amenities and host_verifications a more concise appearance
    # see data quality issues 3-4
    df['host_verifications'] = df['host_verifications'].str.strip('[]').replace({r'(, )|(,)':'/', '\'':''}, regex=True)
    df['amenities'] = df['amenities'].str.strip('{}').replace({r'(, )|(,)':'/', '\"':''}, regex=True)
    
    # remove the dollar signs from currency based features and convert to double dtype
    for feature in features_dict['features_w_dollar_signs']:
        df[feature] = df[feature].str.replace(r'(\$)|(\,)', '', regex=True)
        df[feature] = df[feature].astype('double')
       
    # remove routing numbers from zipcodes
    df['zipcode'] = df['zipcode'].str.replace(r'(-\d+)|(\s\d+)', '', regex=True)
    
    # remove empty features
    df.drop(columns=features_dict['empty_features'], inplace=True)
    
    # make new levels of calendar_updated that are easier to read and have
    # more frequent occurrences
    df['calendar_updated'] = df['calendar_updated'].replace(features_dict['mapper']).str.replace(r'\d+\s+\w+\s*\w+|never', '15', regex=True)
    df['calendar_updated'] = pd.cut(
                                    df['calendar_updated'].astype('int'),
                                    bins=[0, 1, 2, 3, 4, 5, 6, 7, 14, 15],
                                    labels=['0-1', '1-2', '2-3',
                                            '3-4', '4-5', '5-6',
                                             '6-7', '7-14', '14+']
                                    )
    
    # make 'host_response_time' in an interval based ordinal categorical feature
    df['host_response_time'] = df['host_response_time']\
                                                       .replace({'within an hour':1, 'within a few hours':3,
                                                       'within a day': 24, 'a few days or more':72})
    
    df['host_response_time'] = pd.cut(df['host_response_time'],
                                      bins=[0, 1, 3, 24, 72],
                                      labels=['0-1', '1-3', '3-24', '24+']
                                      )
    
    # turn 'review_scores_value' into an ordinal categorical feature
    df['review_scores_value'] = pd.Categorical(df['review_scores_value'], categories=features_dict['reviews_levels'],
                                               ordered=True)
    df['review_scores_value'].cat.add_categories([1.])
    df['review_scores_value'] = pd.Categorical(df['review_scores_value'],
                                               categories=[1., 2., 3., 4., 5., 6. ,7., 8., 9., 10.],
                                               ordered=True
                                              )


def clean_airbnb_calendar(df):
    '''Clean the airbnb_calendar dataset
    
       params:
           df - a Pandas.DataFrame
       returns:
           null - this is an inplace function
    '''
    # 'listing_id' to be converted to a string
    df['listing_id'] = df['listing_id'].astype('object')
    
    # Replace 't' and 'f' with their boolean counterparts
    df['available'] = df['available'].replace({'t':True, 'f':False})
    
    # Remove the $ sign for automatic numeric parsing
    df['price'] = df['price'].str.replace(r'(\$)|(,)', '', regex=True).str.strip().astype('double')

def make_aggregated_dataframe(df, list_of_funcs, names_of_funcs):
    '''Aggregate Airbnb calendar datasetts by property id and merge.
    
       Aggregate Airbnb calendar datasets by property id. Aggregate values will
       be contained in their own data frame. This function will combine all aggregate
       data frames into one data frame.
    '''
    # Drop all rows that have missing price value
    calendar_no_nas = df.dropna(subset=['price']).drop(columns=['available']).copy(deep=True)
    
    # Create dataframe with a single Pandas.Series filled with the property/listing ids
    aggregated_dataframe = pd.DataFrame(data=calendar_no_nas['listing_id'].unique(), columns=['listing_id'])
    
    # Calculate the aggregate for each property id, then merge the result into the aggregated_dataframe.
    # Will end up with a data frame with len(list_of_funcs) + 1.
    for func, name in zip(list_of_funcs, names_of_funcs):
        aggregated_dataframe = aggregated_dataframe.merge(calendar_no_nas.groupby('listing_id').agg(func)['price'].reset_index(name=name), on='listing_id')
    return aggregated_dataframe
