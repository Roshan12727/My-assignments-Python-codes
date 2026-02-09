def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def save_data(data, file_path):
    data.to_csv(file_path, index=False)

def handle_missing_values(data, strategy='mean'):
    if strategy == 'mean':
        return data.fillna(data.mean())
    elif strategy == 'median':
        return data.fillna(data.median())
    elif strategy == 'drop':
        return data.dropna()
    else:
        raise ValueError("Invalid strategy. Choose 'mean', 'median', or 'drop'.")

def encode_categorical(data, columns):
    return pd.get_dummies(data, columns=columns, drop_first=True)

def scale_features(data, scaler):
    return scaler.fit_transform(data)