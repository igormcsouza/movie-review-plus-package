from classifier.preprocessors import DefaultPreprocessors

class LowerCasePreprocessor(DefaultPreprocessors):

    def applyPreprocessors(self, column):
        return [review.lower() for review in column]