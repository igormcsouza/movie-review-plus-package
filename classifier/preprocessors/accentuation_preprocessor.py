import unidecode
from tqdm import tqdm
from nltk import tokenize
from nltk.corpus import stopwords

from classifier.preprocessors import DefaultPreprocessors

class AccentuationPreprocessor(DefaultPreprocessors):

    def apply_preprocessors(self, column):
        irrelevants = stopwords.words("portuguese")
        whiteSpaceTokenizer = tokenize.WhitespaceTokenizer()

        column_2 = [unidecode.unidecode(review) for review in column]
        irrelavantes_without_accentuation = [unidecode.unidecode(each) for each in irrelevants]

        processed_sentece = list()
        for each in tqdm(column_2, desc="AccentuationPreprocessor"):
            filtered_sentence = list()
            wordish = whiteSpaceTokenizer.tokenize(each)
            for item in wordish:
                if item not in irrelavantes_without_accentuation:
                    filtered_sentence.append(item)
            processed_sentece.append(' '.join(filtered_sentence))

        return processed_sentece 