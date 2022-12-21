import requests
from tkinter import Tk, TOP, Label, Entry, X, Button

HEIGHT = '350'
WIDTH = '350'


class CurrencyConvertor:
    def __init__(self, root):
        self.output = None

        root.title("FOREX EXCHANGE CALCULATOR")
        root.geometry('{}x{}+10+10'.format(HEIGHT, WIDTH))
        root.configure(bg='#131417')

        # ====================================================== Label: Input the amounts below
        label_a = Label(root, text="Input the amounts below:")
        label_a.pack(padx=(10, 10), pady=(10, 5), side=TOP, anchor='w')
        label_a.configure(bg='#131417', fg='#308d46', font=("Consolas", 15, 'bold'))

        # ====================================================== Label(I/O): Amount you send (INR)
        label_usd = Label(root, text="Amount you send (INR)")
        label_usd.pack(padx=(20, 10), pady=(10, 5), side=TOP, anchor='w')
        label_usd.configure(bg='#131417', fg='#ffffff', font=("Consolas", 10))
        self.input_usd = Entry(root)
        self.input_usd.pack(padx=(10, 10), pady=(0, 0), side=TOP, anchor='w', fill=X)
        self.input_usd.configure(bg='#575757', fg='#ffffff', font=("Consolas", 10))

        # ====================================================== Label(I/O): FOREX Conversion Rate
        label_bank = Label(root, text="FOREX Conversion Rate")
        label_bank.pack(padx=(20, 10), pady=(10, 5), side=TOP, anchor='w')
        label_bank.configure(bg='#131417', fg='#ffffff', font=("Consolas", 10))
        self.input_bank = Entry(root)
        self.input_bank.pack(padx=(10, 10), pady=(0, 0), side=TOP, anchor='w', fill=X)
        self.input_bank.configure(bg='#575757', fg='#ffffff', font=("Consolas", 10))

        # ====================================================== Label(I/O): You Receive
        label_out = Label(root, text="You Receive:")
        label_out.pack(padx=(20, 10), pady=(10, 5), side=TOP, anchor='w')
        label_out.configure(bg='#131417', fg='#ffffff', font=("Consolas", 10))
        self.output = Label(root, text="$ 0.00")
        self.output.pack(padx=(20, 10), pady=(10, 5), side=TOP, anchor='w')
        self.output.configure(bg='#131417', fg='#ffffff', font=("Consolas", 20))

        # ======================================================  Button: Submit
        button = Button(root, text="Submit", command=self.submit_action)
        button.pack(padx=(10, 10), pady=(30, 0), side=TOP, anchor='w', fill=X)
        button.configure(bg='#2b2b2b', fg='#ec4e20', font=("Consolas", 15))

    def submit_action(self) -> None:
        conversion_rate = self.get_data()
        result = '$ ' + str(round(((int(self.input_usd.get()) / conversion_rate) + int(self.input_bank.get())), 2))
        self.output.configure(text=result)

    @staticmethod
    def get_data():
        url = "https://api.apilayer.com/currency_data/live?source=USD&currencies=INR"
        response = requests.request("GET", url, headers=headers)
        result = response.json()
        print(result)
        return result['quotes']['USDINR']


headers = {
    "apikey":       "EAdk2r9VYNO7AAuZsucnnjtelB7SSpcI",
    "Content-Type": "text/plain"
}

if __name__ == "__main__":
    try:
        window = Tk()
        CurrencyConvertor(window)
        window.mainloop()
    except KeyboardInterrupt:
        exit()
