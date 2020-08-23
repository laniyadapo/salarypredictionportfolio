# Extract Summary info about specified dataframe in argument.

def data_properties(dataframe):
    print('{0:#^80}'.format('Dataset Properties'))
    
    print('\n There are {0} rows and {1} columns'.format(*dataframe.shape))
    
    print('\n{0:#^80}'.format('The columns in the dataset are'))
    
    print(dataframe.columns)
    
    print('\n{0:#^80}'.format('The first 5 rows in the dataset are'))
    
    print(dataframe.head())

    print('\n{0:#^80}'.format('The data types and null values count in the dataset are'))
    
    print(dataframe.info())
    
    print('\n{0:#^80}'.format('The number of duplicates in the dataset'))
    
    print(dataframe.duplicated().sum())
          
    return

# Create data set for Analysis by merging features and variables data
def merge_data(train, train_target):
    merged_train_data = train.merge(train_target, how='left', on='jobId')
    
    return merged_train_data

# Create plots to check correlation of features with the target variable
def plot_feature(df, col):
    '''
    making plot for each feature
    left: the distribution of samples on the feature
    right: the correlation between the feature and salary
    '''
    plt.figure(figsize = (14, 6))
    plt.subplot(1, 2, 1)
    if df[col].dtype == 'int64':
        df[col].value_counts().sort_index().plot()
    elif col == 'companyId':
        mean = df.groupby(col)['salary'].mean()
        levels = mean.sort_values().index.tolist()
        df[col].cat.reorder_categories(levels, inplace = True)
        df[col].value_counts().plot()
    else:
        #plotting the number of jobs under each subcategory of categorial variables
        frequency = df[col].value_counts()
        sub_categories = pd.unique(df[col])
        sns.barplot(x = sub_categories, y = frequency, data = df)
    plt.xticks(rotation = 45)
    plt.xlabel(col)
    plt.ylabel('counts')
    plt.subplot(1, 2, 2)

    if df[col].dtype == 'int64' or col == 'companyId':
        #plot the mean salary for each category and fill between the (mean-std, mean+std)
        mean = df.groupby(col)['salary'].mean()
        std = df.groupby(col)['salary'].std()
        mean.plot()
        plt.fill_between(range(len(std.index)), mean.values-std.values, mean.values + std.values, \
                         alpha = 0.1)
    else:
        sns.boxplot(x = col, y = 'salary', data = df)
    plt.xticks(rotation = 45)
    plt.ylabel('salaries')
    plt.show()