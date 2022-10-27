from tkinter import *
from ui import CurrencyConverterUI
from utils import RealTimeCurrencyConverter

url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConverter(url)

CurrencyConverterUI(converter)
mainloop()

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'

