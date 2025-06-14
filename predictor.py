
import random

class CoinFlipPredictor:
    def __init__(self):
        self.history = []

    def flip_coin(self):
        outcome = random.choice(['Heads', 'Tails'])
        self.history.append(outcome)
        return outcome

    def predict_next(self):
        if not self.history:
            return random.choice(['Heads', 'Tails'])  # no data to predict from

        last_flip = self.history[-1]
        prediction = 'Tails' if last_flip == 'Heads' else 'Heads'
        return prediction

    def get_history(self):
        return self.history
