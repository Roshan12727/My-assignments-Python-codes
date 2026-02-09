def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def make_prediction(model, input_data):
    return model.predict(input_data)

if __name__ == "__main__":
    import pandas as pd
    import sys

    model_path = sys.argv[1]
    input_data_path = sys.argv[2]

    model = load_model(model_path)
    input_data = pd.read_csv(input_data_path)

    predictions = make_prediction(model, input_data)
    print(predictions)