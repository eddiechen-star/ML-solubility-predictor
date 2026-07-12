# works by using a number of bits/trees (2048 in this case) and checking whether to go "right" or "left", determined by 0s and 1s.
from sklearn.ensemble import RandomForestRegressor # predictions
import os
import pickle

def train(x_train, y_train):
    model_path = "data/model.pkl"

    # make sure folder exists
    os.makedirs("data", exist_ok=True)

    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            model = pickle.load(f)

    else:
        # the actual training using the split data
        model = RandomForestRegressor()
        model.fit(x_train, y_train)

        with open(model_path, "wb") as f:
            pickle.dump(model, f)

    return model