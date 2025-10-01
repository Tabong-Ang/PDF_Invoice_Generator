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
    total_amt_entry.delete(0, END)
    total_amt_entry.insert(END, str(calculate_total()))
    update_invoice_text()

def calculate_total():
    total = 0.0
    for item in invoice_items:
        total = total + item[2]
    return total

def update_invoice_text():
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(END, f'Medicine: {item[0]}\nQuantity: {item[1]}\nTotal: {item[2]}\n-------------------\n')

def generate_invoice():
    customer_name = customer_entry.get()

    pdf = FPDF()
    pdf.add_page()

    pdf.cell(0, 10, txt='Invoice', new_x='LMARGIN', new_y='NEXT', align='C')
    pdf.cell(0, 10, txt='Customer: ' + customer_name, new_x='LMARGIN', new_y='NEXT', align='L')
    pdf.cell(0, 10, txt='', new_x='LMARGIN', new_y='NEXT')
    for item in invoice_items:
        medicine_name, quantity, total_item = item
        pdf.cell(0, 10, txt=f'Medicine: {medicine_name}\n Quantity: {quantity}\n Total: {total_item}', 
                new_x='LMARGIN', new_y='NEXT', align='L')
    pdf.cell(0, 10, txt='Total Amount: ' + str(calculate_total()),
            new_x='LMARGIN', new_y='NEXT', align='L')
    pdf.output('invoice.pdf')

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

