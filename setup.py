from tkinter import *
from urllib.request import *
import ast

def apiUpdate():
    xmrPrice = urlopen("https://poloniex.com/public?command=returnTicker" + "&currencyPair=BTC_XMR" + "&currencyPair=USDT_XMR")
    response = xmrPrice.read()
    response = response.decode("utf-8")
    response = ast.literal_eval(response)
    xmrUsd = response["USDT_XMR"]['last']
    xmrBtc = response["BTC_XMR"]['last']
    return [xmrUsd, xmrBtc]

def clickDonate():
    toplevel = Toplevel()
    donateLabel1 = Label(toplevel, text="Donation Address: ", height=0, width=100)
    donateLabel1.pack()
    donateLabel2 = Label(toplevel, text="45a3Qan74Ag4SqYLo7PouD37akLMJCkeWhjfEmL9DwWpPMR9Xyc9XupT1kpb4Tu8hjGoiRBpLpz3dFAWhj2qPPAGQiiAX3N", height=0, width=100)
    donateLabel2.pack()

def updateText():
    prices = apiUpdate()
    labelUsd['text'] = "USD/XMR: $%.7s" % prices[0]+"\n\nBTC/XMR: B"+prices[1]
    root.title("PyXMR Ticker  "+"$%.5s" % prices[0]+"  B%.8s" % prices[1])
    root.after(10000, updateText)



def creatorInfo():
    toplevel2 = Toplevel()
    creatorInfo1 = Label(toplevel2, text="Mine at my pool! @ usxmrpool.com")
    creatorInfo1.pack()
    creatorInfo2 = Label(toplevel2, text="Reddit: /u/ZMC8881")
    creatorInfo2.pack()
    creatorInfo3 = Label(toplevel2, text="Github: ZachC16")
    creatorInfo3.pack()



root = Tk()

root.title("Python XMR Price Tracker")
root.configure(background = "black")
root.geometry("300x200")


app = Frame(root)
app.grid()
labelUsd = Label(app, text = "USD/XMR: Initializing"+"\n\nBTC/XMR: Initializing", fg = "orange", background = "black", padx = 30, pady = 25)
labelUsd.config(font = ("Courier", "20"))
labelUsd.grid()
donateButton = Button(text = "Show Donation Address", width=20, command=clickDonate)
donateButton.configure(background = "black")
donateButton.grid()
creatorInfoButton = Button(text = "Creator Info", width=20, command=creatorInfo)
creatorInfoButton.configure(background = "black")
creatorInfoButton.grid()
updateText()
root.mainloop()

