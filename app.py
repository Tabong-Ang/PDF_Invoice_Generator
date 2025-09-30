from fpdf import FPDF
from tkinter import *


root = Tk()
root.title('Invoice Generator')
root.geometry('500x550')

medicines = {
    'Medicine A': 10,
    'Medicine B': 20,
    'Medicine C': 15,
    'Medicine D': 35,
    'Medicine E': 15,
    'Medicine F': 45,
    'Medicine G': 26,
}

invoice_items = []

def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)
    qty = int(qty_entry.get())
    price = medicines[selected_medicine]
    total_item = price * qty
    invoice_items.append((selected_medicine, qty, total_item))
    print(invoice_items)

medicine_label = Label(root, text='Medicine')
medicine_label.pack()

medicine_listbox = Listbox(root, selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END, medicine)
medicine_listbox.pack()

qty_label = Label(root, text='Quantity')
qty_label.pack()

qty_entry = Entry(root)
qty_entry.pack()

add_btn = Button(root, text='Add Medicine', command=add_medicine)
add_btn.pack()

total_amt_label = Label(root, text='Total Amount')
total_amt_label.pack()

total_amt_entry = Entry(root)
total_amt_entry.pack()

customer_label = Label(root, text='Customer Name: ')
customer_label.pack()

customer_entry = Entry(root)
customer_entry.pack()

generate_btn = Button(root, text='Generate Invoice')
generate_btn.pack()

invoice_text = Text(root, height=10, width=50)
invoice_text.pack()


pdf = FPDF()
root.mainloop()

