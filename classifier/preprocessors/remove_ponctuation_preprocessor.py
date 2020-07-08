from tqdm import tqdm
from nltk import tokenize
from string import punctuation

from classifier.preprocessors import DefaultPreprocessors

class RemovePonctuationPreprocessor(DefaultPreprocessors):

    def apply_preprocessors(self, column):
        punctuationTokenizer = tokenize.WordPunctTokenizer()

        processed_sentece = list()
        for each in tqdm(column, desc="RemovePonctuationPreprocessor"):
            filtered_sentence = list()
            wordish = punctuationTokenizer.tokenize(each)
            for item in wordish:
                if item not in [p for p in punctuation]:
                    filtered_sentence.append(item)
            processed_sentece.append(' '.join(filtered_sentence))

        return processed_sentece