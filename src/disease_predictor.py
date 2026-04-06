class DiseasePredictor:
    def __init__(self, model):
        self.model = model

    def predict(self, input_data):
        # Implement prediction logic
        return self.model.predict(input_data)