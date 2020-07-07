from classifier.preprocessors import DefaultPreprocessors

class LowerCasePreprocessor(DefaultPreprocessors):

    def apply_preprocessors(self, column):
        column_2 = [unidecode.unidecode(review) for review in column]
        irrelavantes_without_accentuation = [unidecode.unidecode(each) for each in irrelevants]

        processed_sentece = list()
        for each in tqdm(reviews['preprocess_2']):
            filtered_sentence = list()
            wordish = whiteSpaceTokenizer.tokenize(each)
            for item in wordish:
                if item not in irrelavantes_without_accentuation:
                    filtered_sentence.append(item)
            processed_sentece.append(' '.join(filtered_sentence))

        reviews['preprocess_2'] = processed_sentece 