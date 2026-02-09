def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    evaluation_results = {
        'Mean Squared Error': mse,
        'Mean Absolute Error': mae,
        'R-squared': r2
    }

    return evaluation_results

def print_evaluation_results(results):
    for metric, value in results.items():
        print(f"{metric}: {value:.4f}")

# Example usage:
# if __name__ == "__main__":
#     from sklearn.model_selection import train_test_split
#     from sklearn.ensemble import RandomForestRegressor
#     import pandas as pd

#     # Load your dataset
#     data = pd.read_csv('path_to_your_processed_data.csv')
#     X = data.drop('target_column', axis=1)
#     y = data['target_column']

#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#     model = RandomForestRegressor()
#     model.fit(X_train, y_train)

#     results = evaluate_model(model, X_test, y_test)
#     print_evaluation_results(results)