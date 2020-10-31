from tkinter import *

converter=Tk()
converter.geometry("700x300",)

converter.title("CURRENCY CONVERTER")

OPTIONS={
    		
      "Algerian Dinar":0.5795,
      "American Dollar":74.61,
      "Argentine Peso":0.953,
      "Australian Dollar":52.45,
      "Bitcoin":1036178,
      "Brazilian Real":12.99,
      "British Pound":96.59,
      "Bulgarian Lev":44.47,
      "Canadian Dollar":56.01,
      "Chilean Peso":0.0965,
      "Chinese Yuan Renminbi":11.15,
      "Croatian Kuna":11.48,
      "Czech Koruna":3.191,
      "Danish Krone":11.67,
      "Egyptian Pound":4.764,
      "Ethereum":29272,
      "Euro":87.13,
      "Hong Kong Dollar":9.623,
      "Hungarian Forint":0.2372,
      "Iceland Krona":0.529,
      "Indonesian Rupiah":0.0051,
      "Iranian Rial":0.0018,
      "Israeli New Shekel":21.9,
      "Japanese Yen":0.713,
      "Korean Won":0.0656,
      "Malaysian Ringgit":17.97,
      "Mexican Peso":3.522,
      "New Zealand Dollar":49.35,
      "Nigerian Naira":0.1961,
      "Norwegian Krone":7.842,
      "Pakistan Rupee":0.465,
      "Philippine Peso":1.541,
      "Polish Zloty":18.86,
      "Qatari Rial":20.49,
      "Romanian Leu":17.87,
      "Russian Ruble":0.9401,
      "Saudi Riyal":19.9,
      "Serbian Dinar":0.739,
      "Singapore Dollar":54.62,
     
    
     
    }
def ok():
    price=rupees.get()
    answer=variable.get()
    DICT=OPTIONS.get(answer,None)
    
    converted=float(price)/float(DICT)
    result.delete(1.0,END)
    result.insert(INSERT,"Amount in ",INSERT,answer,INSERT," = ",
                  INSERT,converted)
    
Name= Label(converter,text="CURRENCY",
              font=("georgia",25,"bold"),fg="dark blue")
Name.grid(row=0,column=0)
Name= Label(converter,text="CONVERTER",
              font=("georgia",25,"bold"),fg="dark blue")
Name.grid(row=0,column=1,ipadx=10)

india=Label(converter,text="Indian Rupee" ,
            font=("century",18),fg="black")
india.grid(row=1,column=0)
rupees=Entry(converter,font=("calibri",15))
rupees.grid(row=1,column=1)
choice=Label(converter,text="Choose Currency",
            font=("century",18),fg="black")
choice.grid(row=2,column=0)
variable = StringVar(converter)
variable.set(None)
option=OptionMenu(converter,variable,*OPTIONS)
option.grid(row=2,column=1,sticky="ew")
button=Button(converter,text="convert",fg="black",
              font=("calibri,12"),command=ok)
button.grid(row=3,column=1)
var=Label(converter,text ="  Converted Amount",
          font=("century",18),fg="black")
var.grid(row=4,column=0)
result=Text(converter,height=3,width=45,font=("arial",12),bd=1)
result.grid(row=4,column=1,padx=3)
mainloop()
