import re

from tkinter import (
    Label,
    StringVar,
    Button,
    Entry,

    RIDGE,
    CENTER,
    RAISED,
    GROOVE,

    ttk,
    Tk,
)


class CurrencyConverterUI(Tk):
    def __init__(self, converter):
        Tk.__init__(self)

        self.title = 'Currency Converter'
        self.currency_converter = converter
        self.geometry("500x200")

        self.intro_label = Label(
            self,
            text='Welcome to Real Time Currency Convertor',
            fg='orange',
            bg='black',
            relief=RAISED,
            borderwidth=3
        )
        self.intro_label.config(font=('Courier', 15, 'bold'))
        self.date_label = Label(
            self,
            text=f"1 Polish Zloty equals = "
                 f"{self.currency_converter.convert('PLN', 'USD', 1)} USD \n "
                 f"Date : {self.currency_converter.data['date']}",
            fg='orange',
            bg='black',
            relief=GROOVE, borderwidth=5
        )
        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=170, y=50)

        valid = (self.register(self.restrictNumberOnly), '%d', '%P')

        self.amount_field = Entry(
            self,
            bd=3,
            relief=RIDGE,
            justify=CENTER,
            validate='key',
            validatecommand=valid
        )
        self.converted_amount_field_label = Label(
            self, text='',
            fg='black',
            bg='white',
            relief=RIDGE,
            justify=CENTER,
            width=20,
            borderwidth=3
        )

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("PLN")
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(
            self,
            textvariable=self.from_currency_variable,
            values=list(self.currency_converter.currencies.keys()),
            font=font,
            state='readonly',
            width=12,
            justify=CENTER
        )
        self.to_currency_dropdown = ttk.Combobox(
            self,
            textvariable=self.to_currency_variable,
            values=list(self.currency_converter.currencies.keys()),
            font=font,
            state='readonly',
            width=12,
            justify=CENTER
        )

        # placing
        self.from_currency_dropdown.place(x=30, y=120)
        self.amount_field.place(x=28, y=150)
        self.to_currency_dropdown.place(x=340, y=120)
        self.converted_amount_field_label.place(x=338, y=150)

        # Convert button
        self.convert_button = Button(
            self,
            text="Convert",
            fg="black",
            command=self.perform
        )
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=225, y=135)

    def perform(self, ):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text=str(converted_amount))

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (
                string == ""
                or
                (string.count('.') <= 1 and result is not None)
        )
