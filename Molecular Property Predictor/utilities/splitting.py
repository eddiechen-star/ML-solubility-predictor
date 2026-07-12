# what the model learns from and what the model is "graded" on
from sklearn.model_selection import train_test_split

def split(x_features, y):
    # splitting the data into training or test data
    x_train, x_test, y_train, y_test = train_test_split(
        x_features,
        y,
        test_size=0.2,       # 20% of data goes to the test set, 80% to train
        random_state=42,     # predictable outcomes
        shuffle=True         # shuffles data before splitting
    )
    return x_train, x_test, y_train, y_test