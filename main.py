

from tkinter import Text, Tk
from tkinter import *
root = Tk(className=' Amzer Capital Stock Trader Version 3')
root.geometry("1800x940")
root.resizable(0, 0)

'''
my_menu = Menu(root)
root.config(menu=my_menu)
'''
'''
def new_command():
    pass
def open_command():
    pass
file_menu  = Menu(my_menu)
my_menu.add_cascade(label = 'File',menu = file_menu)
file_menu.add_command(label = 'New',command = new_command)
file_menu.add_separator()
file_menu.add_command(label='Open',command = open_command)
'''

buy_price_text = Entry(root,width = 10, font = 'Times 50')
buy_price_text.place(x=400,y=200)
buy_price_text.insert(0,'')

qty_price_text = Entry(root,width = 10, font = 'Times 50')
qty_price_text.place(x=400,y=330)
qty_price_text.insert(0,'')

stop_price_text = Entry(root,width = 10, font = 'Times 50')
stop_price_text.place(x=400,y=460)
stop_price_text.insert(0,'')

sell1_price_text = Entry(root,width = 10, font = 'Times 50')
sell1_price_text.place(x=400,y=590)
sell1_price_text.insert(0,'')

sell2_price_text = Entry(root,width = 10, font = 'Times 50')
sell2_price_text.place(x=400,y=670)
sell2_price_text.insert(0,'')

sell3_price_text = Entry(root,width = 10, font = 'Times 50')
sell3_price_text.place(x=400,y=750)
sell3_price_text.insert(0,'')



def click():
    hello = (float(buy_price_text.get()))*(int(qty_price_text.get()))
    disp_buy_price = Label(root,text = ('Total $ Invested:',hello), font = 'Times 50')
    disp_buy_price.place(x=800,y=265)
    
    if stop_price_text.get() !='':
        empty = Label(root,text = ('                                                            '), font = 'Times 50')
        empty.place(x=800,y=460)
        stop_cost = ((float(stop_price_text.get()) - float(buy_price_text.get()))*(int(qty_price_text.get())))
        aaa = Label(root,text = ('Stop Loss:'), font = 'Times 50')
        disp_buy_price = Label(root,text = (stop_cost), font = 'Times 50',fg = 'red')
        if (sell1_price_text.get() == ''):
            dd = Label(root,text = ('                                                            '), font = 'Times 50')
            dd.place(x=800,y=590)
        disp_buy_price.place(x=1200,y=460)
        aaa.place(x=800,y=460)
        
    if ((sell2_price_text.get()) and (sell3_price_text.get())) == '':
        empty = Label(root,text = ('                                                            '), font = 'Times 50')
        empty.place(x=800,y=590)
        sell1_cost = ((float(sell1_price_text.get()) - float(buy_price_text.get()))*(int(qty_price_text.get())))
        bb = Label(root,text = ('Target Price 1:'), font = 'Times 50')
        bbb = Label(root,text = (sell1_cost), font = 'Times 50',fg = 'green')
        if (sell2_price_text.get() == ''):
            dd = Label(root,text = ('                                                            '), font = 'Times 50')
            dd.place(x=800,y=670)
        bb.place(x=800,y=590)
        bbb.place(x=1200,y=590)
    
    if (sell3_price_text.get() == '') and (sell2_price_text.get() != '') and (sell1_price_text.get() !=''):
        empty = Label(root,text = ('                                                            '), font = 'Times 50')
        empty.place(x=800,y=670)
        empty = Label(root,text = ('                                                            '), font = 'Times 50')
        empty.place(x = 800,y=590)
        sell1_and_2_cost = ((float(sell1_price_text.get()) - float(buy_price_text.get()))*((int(qty_price_text.get()))/2) + ((float(sell2_price_text.get()) - float(buy_price_text.get()))*((int(qty_price_text.get()))/2)))
        cc = Label(root,text = ('Target Price 2:'), font = 'Times 50')
        ccc = Label(root,text = (sell1_and_2_cost), font = 'Times 50',fg = 'green')
        if (sell3_price_text.get() == ''):
            dd = Label(root,text = ('                                                            '), font = 'Times 50')
            dd.place(x=800,y=750) 
            
        cc.place(x=800,y=670)
        ccc.place(x=1200,y=670)
        
    if (sell3_price_text.get() != '') and (sell2_price_text.get() != '') and (sell1_price_text.get() !=''):
        empty = Label(root,text = ('                                                            '), font = 'Times 50')
        empty.place(x=800,y=590)
        empty.place(x=800,y=670)
        empty.place(x=800,y=750)
        sell1_and_2_and_3_cost = ((float(sell1_price_text.get()) - float(buy_price_text.get()))*((int(qty_price_text.get()))/2) + ((float(sell2_price_text.get()) - float(buy_price_text.get()))*((int(qty_price_text.get()))/4)))+((float(sell3_price_text.get()) - float(buy_price_text.get()))*((int(qty_price_text.get()))/4))
        ee = Label(root,text = ('Target Price 3:'), font = 'Times 50')
        eee = Label(root,text = (sell1_and_2_and_3_cost), font = 'Times 50',fg = 'green')
        ee.place(x=800,y=750) 
        eee.place(x=1200,y=750)

    
    
    
    
    
buy_price_button = Button(root,text = 'Enter',font = 'Times 40',command = click)
buy_price_button.place(x = 500,y=820)


stock = Label(root,text = 'STOCK',font = 'Times 100')


buy_price = Label(root,text = 'BUY PRICE:',font = 'Times 50')
qty = Label(root,text = 'QUANTITY:',font = 'Times 50')
stop = Label(root,text = 'STOP:',font = 'Times 50')
sell1 = Label(root,text = 'TP1:',font = 'Times 50')
sell2 = Label(root,text = 'TP2:',font = 'Times 50')
sell3 = Label(root,text = 'TP3:',font = 'Times 50')

stock.place(x = 730,y= 20)


buy_price.place(x=30,y=200)
qty.place(x=30,y=330)
stop.place(x=30,y=460)
sell1.place(x=30,y=590)
sell2.place(x=30,y=670)
sell3.place(x=30,y=750)
'''
Jam = Button(root, text = 'The Jam', width = 25, height = 2)
Jam.grid(row=0, column=0, pady = 10, padx = 25, sticky=W)
'''



root.mainloop()


#((float(stop_price_text.get()) - float(buy_price_text.get()))/(float(buy_price_text.get())))*(float(buy_price_text.get()))*(int(qty_price_text.get()))
 







'''

def click():
    hello = (float(buy_price_text.get()))*(int(qty_price_text.get()))
    disp_buy_price = Label(root,text = hello, font = 'Times 50')
    disp_buy_price.place(x=1100,y=265)
    
    if stop_price_text.get() !='':
        stop_cost = ((float(stop_price_text.get()) - float(buy_price_text.get()))*(int(qty_price_text.get())))
        disp_buy_price = Label(root,text = stop_cost, font = 'Times 50')
        disp_buy_price.place(x=1100,y=400)
        
        if ((sell2_price_text.get()) and (sell3_price_text.get())) == '':
            sell1_cost = ((float(sell1_price_text.get()) - float(buy_price_text.get()))*(int(qty_price_text.get())))
            bb = Label(root,text = sell1_cost, font = 'Times 50')
            bb.place(x=1100,y=600)

    elif ((sell2_price_text.get()) and (sell3_price_text.get())) == '':
        sell1_cost = ((float(sell1_price_text.get()) - float(buy_price_text.get()))*(int(qty_price_text.get())))
        bb = Label(root,text = sell1_cost, font = 'Times 50')
        bb.place(x=1100,y=600)
  
    

'''

