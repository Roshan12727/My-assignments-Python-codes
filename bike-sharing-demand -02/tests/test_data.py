# test_data.py

import unittest
import pandas as pd
from src.data.preprocess import clean_data, handle_missing_values

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        self.raw_data = pd.DataFrame({
            'datetime': ['2021-01-01 00:00:00', '2021-01-01 01:00:00', None],
            'temperature': [9.84, 9.02, 9.12],
            'humidity': [81, 80, None],
            'windspeed': [0.0, 0.0, 0.0],
            'count': [16, 40, 32]
        })

    def test_clean_data(self):
        cleaned_data = clean_data(self.raw_data)
        self.assertEqual(cleaned_data.isnull().sum().sum(), 0)

    def test_handle_missing_values(self):
        filled_data = handle_missing_values(self.raw_data)
        self.assertFalse(filled_data['humidity'].isnull().any())

if __name__ == '__main__':
    unittest.main()