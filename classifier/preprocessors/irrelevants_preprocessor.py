from nltk.corpus import stopwords

from classifier.preprocessors import DefaultPreprocessors


class IrrelevantsPreprocessor(DefaultPreprocessors):

    def applyPreprocessors(self, column):
        irrelevants = stopwords.words("portuguese")

        processed_sentece = list()
        for each in tqdm(column):
            filtered_sentence = list()
            wordish = whiteSpaceTokenizer.tokenize(each)
            for item in wordish:
                if item not in irrelevants:
                    filtered_sentence.append(item)
            processed_sentece.append(' '.join(filtered_sentence))

        return processed_sentece
