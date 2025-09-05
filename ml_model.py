import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_predict(df):
    df = df.dropna()
    features = df[['RSI', '20DMA', '50DMA', 'Volume']]
    labels = (df['Close'].shift(-1) > df['Close']).astype(int)


    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, shuffle=False)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)


    acc = accuracy_score(y_test, preds)
    return model, acc