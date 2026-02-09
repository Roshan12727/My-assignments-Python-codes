from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import mean_squared_error
import joblib

def hyperparameter_tuning(model, param_grid, X_train, y_train, search_type='grid', n_iter=10, cv=5):
    if search_type == 'grid':
        search = GridSearchCV(model, param_grid, n_jobs=-1, cv=cv, scoring='neg_mean_squared_error')
    elif search_type == 'random':
        search = RandomizedSearchCV(model, param_distributions=param_grid, n_jobs=-1, n_iter=n_iter, cv=cv, scoring='neg_mean_squared_error', random_state=42)
    else:
        raise ValueError("search_type must be either 'grid' or 'random'")

    search.fit(X_train, y_train)
    best_model = search.best_estimator_
    best_params = search.best_params_
    best_score = -search.best_score_

    return best_model, best_params, best_score

def save_best_model(model, filename):
    joblib.dump(model, filename)

def load_best_model(filename):
    return joblib.load(filename)