from tkinter import mainloop
from ui import CurrencyConverterUI
from utils import RealTimeCurrencyConverter

URL = 'https://api.exchangerate-api.com/v4/latest/USD'

if __name__ == '__main__':
    converter = RealTimeCurrencyConverter(URL)
    CurrencyConverterUI(converter)
    mainloop()
