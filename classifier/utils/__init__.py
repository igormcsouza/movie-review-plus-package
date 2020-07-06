import pandas as pd
import seaborn as sns
from nltk import tokenize,FreqDist
from matplotlib import pyplot as plt

def get_occurs_df(dataset, column):
    """ Get words occurencies on a dataset

    :dataset: Pandas DataFrame where the text is.
    :column: Column where the text is to be count

    :return: DataFrame of occurrencies of each word in the dataset column
    
    """

    whiteSpaceTokenizer = tokenize.WhitespaceTokenizer()

    all_words = ' '.join([item for item in dataset[column]])
    review_tokens = whiteSpaceTokenizer.tokenize(all_words)
    occurencies = FreqDist(review_tokens)

    return pd.DataFrame({
        'words': list(occurencies.keys()), 
        'occur': list(occurencies.values())
    })

def plot_samples(df, n=10):
    """ Show on screen the Plot of Words Occurrencies

    :df: Pandas DataFrame where with the words occurrencies
    :n: Number of words to the shown

    :behavior: Show on screen a barplot with the number of words 
    from the biggest to the n-ist biggest

    :return: Nothing
    
    """

    plt.figure(figsize=(12,8))
    ax = sns.barplot(data=df.nlargest(columns='occur', n=n), x="words", y="occur", color='green')
    ax.set(ylabel='Count')
    plt.show()