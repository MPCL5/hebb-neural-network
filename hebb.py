class Hebb:
    @staticmethod
    def get_new_weight(old, x, result):
        return old + x * result

    def __init__(self, input_count, actice_function):
        self.input_count = input_count
        self.weights = [0 for item in range(input_count)]
        self.bias = 0
        self.actice_function = actice_function

    def train_one(self, inputs, result):
        # Step.5
        for i in range(len(inputs)):
            self.weights[i] = Hebb.get_new_weight(
                self.weights[i], inputs[i], result)
        # Step.6
        self.bias = Hebb.get_new_weight(self.bias, 1, result)
        # simplify the weights
        # self.evenWeights()

    def train_all(self, cases):
        for case in cases:
            self.train_one(case['inputs'], case['result'])

    def get_weights(self):
        return self.weights

    def get_bias(self):
        return self.bias

    def predict_one(self, inputs):
        result = 0
        for i in range(len(self.weights)):
            result += self.weights[i] * inputs[i]

        result += self.bias
        return self.actice_function(result)
