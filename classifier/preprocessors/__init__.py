import nltk

nltk.download('stopwords')
nltk.download('rslp')

class DefaultPreprocessors:

    def __init__(self, column):
        self.column = column

    def applyPreprocessors(self):
        pass