import matplotlib.pyplot as plt

def draw_graph(data, prediction):

    plt.figure(figsize=(12,6))

    plt.plot(data["Close"], label="Gerçek Fiyat")

    plt.axhline(
        y=prediction,
        color='red',
        linestyle='--',
        label='Tahmin'
    )

    plt.title("Hisse Analizi")

    plt.xlabel("Tarih")
    plt.ylabel("Fiyat")

    plt.legend()

    plt.show()