from data_fetch import get_stock_data
from predictor import predict_price
from graph import draw_graph

stock = input("Hisse kodu gir: ")

data = get_stock_data(stock)

prediction = predict_price(data)

current_price = float(data["Close"].iloc[-1])

prediction = float(prediction)

print("Güncel:", current_price)
print("Tahmin:", prediction)

if prediction > current_price:
    print("AL")
else:
    print("SAT")

draw_graph(data, prediction)