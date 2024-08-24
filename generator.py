import random
import pandas as pd


def decoder(pin):
    """
    fuck docstrings
    """

    w1 = 5
    w2 = 20
    b = 30

    return w1 * pin**2 + w2 * pin + b


decoded = [random.randint(0, 100) for i in range(100000)]
encoded = [decoder(pin) for pin in decoded]

df = pd.DataFrame({'decoded': decoded, 'encoded': encoded})
df.to_csv("./samples.csv")
