from sklearn.model_selection import train_test_split

class ModelTrainer:
    def __init__(self, model, X, y):
        self.model = model
        self.X = X
        self.y = y

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2)
        self.model.fit(X_train, y_train)
        return self.model.score(X_test, y_test)