# with open('currencyData.txt') as f:
#     lines = f.readlines()
    
# currencyDict = {}
# for line in lines:
#     parsed = line.split("\t")
#     currencyDict[parsed[0]] = parsed[1]


# amount = int(input("Enter amount:\n"))
# print("Enter the name of currency you want to convert this amount to? Available Options:\n")
# [print(item) for item in currencyDict.keys()]

# currency = input("Please enter one of these values: \n")
# print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")


import requests,json
import tkinter as tk
from tkinter import * 

def createWidgets():
    
    country_list = ["India(INR)","United States of America(USD)","Canada(CAD),China(CNY)","European Union(EUR)","Afghanistan(AFN)","Albania(ALL)","Algeria(DZD)","Angola(AOA)","Anguilla(XCD)","Argentina(ARS)","Armenia(AMD)","Aruba(AWG)","Australia(AUD)","Bahamas(BSD)","Brlarus(BYN)","Benin(XOF)","Bhutan(BTN)","Bolivia(BOB)","Colombia(COP)","Comoros(KMF)"]
    
    text_label = Label(root, text="Welcome to python currency converter",bg="#E8D579")
    text_label.grid(row=1,column=1,pady=10)
    
    amount_label = Label(root,text="Enter amount: ",bg="#E8D579")
    amount_label.grid(row=2, column=0, padx=20, pady=10)
    global amount_entry
    amount_entry = Entry(root, width=40, textvariable=amount1)
    amount_entry.grid(row=2, column=1,padx=20,pady=10)
    
    from_country = Label(root, text="From Country: ", bg="#E8D579")
    from_country.grid(row=3, column=0, padx=20,pady=10)
    
    from_menue = OptionMenu(root, variable1, *country_list)
    from_menue.grid(row=3, column=1,padx=20,pady=10)
    
    to_country = Label(root, text="To Country: ", bg="#E8D579")
    to_country.grid(row=4, column=0, padx=20,pady=10)
    
    to_menue = OptionMenu(root, variable2, *country_list)
    to_menue.grid(row=4, column=1,padx=20,pady=10)
    
    convert_but = Button(root, width=15, text="Convert", command=Calculate,bg="#05E8E0")
    convert_but.grid(row=4,column=2,padx=20,pady=10)
    
    converted_text = Label(root, text="Converted Amount: ", bg="#E8D579")
    converted_text.grid(row=5,column=0,padx=20,pady=10)
    
    global amount_entry2
    amount_entry2 = Entry(root, width=40)
    amount_entry2.grid(row=5,column=1,pady=10)
    
    clear_but = Button(root,text="Clear",width=10,command=clear,bg="#05E8E0")
    clear_but.grid(row=5,column=2,pady=10)

def data(str):
    for i in str:
        if i=="(":
            start = str.index(i)+1
        if i==")":
            end = str.index(i)
            
    return str[start:end]

def Calculate():
    
    api_Key="WVNHB0SLFX5H9ORI"
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    var1 = data(variable1.get())
    var2 = data(variable2.get())
    
    main_url = base_url+"&from_currency="+var1+"&to_currency="+var2+"&apikey="+api_Key
    print(main_url)
    
    req_ob = requests.get(main_url)
    result = req_ob.json()
    print(result)
    Exchange_rate = float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    amount = float(amount1.get())
    new_amount = round(amount*Exchange_rate, 3)
    
    amount_entry2.insert(0, str(new_amount))
 

def clear():
    
    amount_entry.delete(0,END)
    amount_entry2.delete(0,END)
    
 

root = tk.Tk()
root.geometry("750x250")
root.title("Currency Converter")
root.config(background="black")

amount1= StringVar()
variable1 = StringVar()
variable2 = StringVar()
variable1.set("From Country")
variable2.set("To Country")

createWidgets()

root.mainloop()