import unittest
from src.models.train import train_model
from src.models.evaluate import evaluate_model
from src.models.predict import make_predictions

class TestModel(unittest.TestCase):

    def setUp(self):
        self.model = train_model()
        self.test_data = ...  # Load or create test data
        self.expected_output = ...  # Define expected output for predictions

    def test_model_training(self):
        self.assertIsNotNone(self.model, "Model should be trained and not None")

    def test_model_evaluation(self):
        metrics = evaluate_model(self.model, self.test_data)
        self.assertIn('rmse', metrics, "Metrics should contain RMSE")
        self.assertGreater(metrics['rmse'], 0, "RMSE should be greater than 0")

    def test_model_prediction(self):
        predictions = make_predictions(self.model, self.test_data)
        self.assertEqual(len(predictions), len(self.test_data), "Predictions length should match test data length")
        self.assertAlmostEqual(predictions.mean(), self.expected_output.mean(), delta=0.1, 
                               msg="Predictions should be close to expected output")

if __name__ == '__main__':
    unittest.main()