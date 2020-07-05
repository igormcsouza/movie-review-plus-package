from classifier.preprocessors import DefaultPreprocessors

class LowerCasePreprocessor(DefaultPreprocessors):

    def applyPreprocessors(self):
        return [review.lower() for review in self.column]