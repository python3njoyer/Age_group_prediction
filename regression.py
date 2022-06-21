import pandas as pd
import torch
import numpy as np


# initialize path variables as input for function below
lexicon_paths = ['age_bins.13_18.gender_adjusted.rmatrix.top100s.csv', 'age_bins.19_22.gender_adjusted.rmatrix.top100s.csv',
                 'age_bins.23_29.gender_adjusted.rmatrix.top100s.csv', 'age_bins.30_+.gender_adjusted.rmatrix.top100s.csv']
tweets_path = 'Zendaya_cleaned.txt'


# reads CSV data (from the World Well-Being Project's lexica). Creates dataframe for each age bin.
def element_mult(list, tweets):
    y_values = []
    for file in list:
        df_13 = pd.read_csv(file, sep=',', skiprows=1)
        print('Raw Data Table:\n', df_13.head())

        # retrieve feature r-values from dataframe, convert into tensor (matrix)
        feat_values = torch.tensor((df_13.iloc[:, 2]))

        # load cleaned tweet data
        with open(tweets) as tweets_file:
            tweets_data = tweets_file.read()

        # create matrix with the frequency count of each feature for tweet set
        freq_list = []
        for lexicon in df_13.iloc[:, 1]:
            print(lexicon + ':', tweets_data.count(lexicon), end='; ')
            freq_list.append(tweets_data.count(lexicon))
        print('\n')

        freq_tensor = torch.Tensor(freq_list)

        # check that the matrices are same dimension
        print(freq_tensor.size(), feat_values.size())

        # elem-wise multiply feature matrix and word frequency matrix together, then sum resulting matrix
        product_mtrx = torch.mul(feat_values, freq_tensor)
        y = torch.sum(product_mtrx)
        y_values.append(y.tolist())  # add final value to list
        print(y_values)

        print('----------------------------------------------------------------------\n')

    return y_values


# normalizes the list of y hats and treats them as probabilities
def soft_max(values):
    out = np.exp(values) / np.sum(np.exp(values))
    return out


# iterate through list of age groups and gives softmax values for each one
def generate_report(inp):
    age_groups = ["13-18", "19-22", "23-29", "30+"]
    print("-----------------Generated Report-----------------")
    print('Probable age group of user:')
    for i in range(len(age_groups)):
        print(f'Age group {age_groups[i]}', ':', f'{inp[i]:.3f}')  # formats percentages as percentages


# call functions to produce score for each age bin
output = element_mult(lexicon_paths, tweets_path)
output = soft_max(output)
generate_report(output)
