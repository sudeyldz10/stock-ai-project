import numpy as np
from sklearn.linear_model import LinearRegression

def predict_price(data):

    close = np.array(data["Close"]).reshape(-1)

    if len(close) < 2:
        return float(close[-1])

    X = close[:-1].reshape(-1, 1)
    y = close[1:]

    model = LinearRegression()
    model.fit(X, y)

    last_price_value = float(close[-1])   # 🔥 EN ÖNEMLİ FIX

    prediction = model.predict([[last_price_value]])  # sadece 2D

    return float(prediction[0])