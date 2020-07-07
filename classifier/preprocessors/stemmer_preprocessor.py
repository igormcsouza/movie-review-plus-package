import nltk
from tqdm import tqdm
from nltk import tokenize

from classifier.preprocessors import DefaultPreprocessors

class StemmerPreprocessor(DefaultPreprocessors):

    def apply_preprocessors(self, column):
        stemmer = nltk.RSLPStemmer()
        whiteSpaceTokenizer = tokenize.WhitespaceTokenizer()

        processed_sentece = list()
        for each in tqdm(column, desc="StemmerPreprocessor"):
            filtered_sentence = list()
            wordish = whiteSpaceTokenizer.tokenize(each)
            for item in wordish:
                filtered_sentence.append(stemmer.stem(item))
            processed_sentece.append(' '.join(filtered_sentence))

        return processed_sentece   