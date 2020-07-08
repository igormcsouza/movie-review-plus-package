from classifier.preprocessors import DefaultPreprocessors

class LowerCasePreprocessor(DefaultPreprocessors):

    def apply_preprocessors(self, column):
        return [review.lower() for review in column]