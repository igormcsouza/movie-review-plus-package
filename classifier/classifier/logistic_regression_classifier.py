import os
import pickle
from joblib import dump, load
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from classifier.classifier import DefaultClassifier


class LogisticRegressionClassifier(DefaultClassifier):

    def initialize_it(self, column, labels, max_features):
        self.vectorizer = TfidfVectorizer(
            max_features=max_features)  # max_features=100

        self.bow = self.vectorizer.fit_transform(column)
        print("Bag of words shape", self.bow.shape)

        # If you want to put everything on a sparse DataFrame, but is not a good idea!
        # df_bow = pd.DataFrame.sparse.from_spmatrix(bow, columns=vectorizer.get_feature_names())

        self.trX, self.teX, self.trY, self.teY = train_test_split(
            self.bow, labels.values.reshape(-1, 1), random_state=9)
        print("Train and Test X shapes:", self.trX.shape, self.teX.shape)
        print("Train and Test Y shapes:", self.trY.shape, self.teY.shape)

    def load(self, regressor_path, vectorizer_path):

        if regressor_path == None or regressor_path.split(.)[-1] != 'joblib':
            raise Exception("The Regressor path is not right! Make sure it has .joblib")

        if vectorizer_path == None or vectorizer_path.split(.)[-1] != 'pickle':
            raise Exception("The Regressor path is not right! Make sure it has .pickle")

        self.regressor = load(regressor_path)
        self.vectorizer = pickle.load(open(vectorizer_path, "rb"))

        return self

    def train(self, solver="lbfgs"):

        self.regressor = LogisticRegression(solver=solver)
        self.regressor.fit(self.trX, self.trY.ravel())

        self.acc = self.regressor.score(self.teX, self.teY.ravel())
        print("acc:", self.acc)

        return self

    def predict(self, phrase):

        if self.regressor == None:
            raise Exception(
                "Regressor wasn't fit yet, please run .train() to make it.")

        if self.vectorizer == None:
            raise Exception("Vectorizer wasn't ready, internal error.")

        return 'pos' if self.regressor.predict(self.vectorizer.transform([phrase]))[0] else 'neg'

    def persist(self, path='', alias=''):

        if self.regressor == None:
            raise Exception(
                "Regressor wasn't fit yet, please run .train() to make it.")

        if self.vectorizer == None:
            raise Exception("Vectorizer wasn't ready, internal error.")

        dump(self.regressor, os.path.join(
            path, "{}-sklearn-logistc-regressor-model.joblib".format(alias)))
        pickle.dump(self.vectorizer, open(os.path.join(
            path, "{}-vectorizer.pickle".format(alias), "wb")))

        return self
