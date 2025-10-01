from fpdf import FPDF
from tkinter import *
import sys, os

def resource_path(relative_path):
    try:
        base_path = sys.MEIPass
    except Exception:
        base_path = os.path.abspath('.')
        return os.path.join(base_path, relative_path)

root = Tk()
root.title('Invoice Generator')
root.geometry('600x600')
root.configure(bg='#f7f9fc')
root.iconbitmap(resource_path('images/photo.ico'))
font_main = ("Segoe UI", 11)
font_title = ("Segoe UI", 14, "bold")

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
    pdf.set_font('helvetica', size=12)

    pdf.cell(0, 10, text='Invoice', new_x='LMARGIN', new_y='NEXT', align='C')
    pdf.cell(0, 10, text='Customer: ' + customer_name, new_x='LMARGIN', new_y='NEXT', align='L')
    pdf.cell(0, 10, text='', new_x='LMARGIN', new_y='NEXT')
    for item in invoice_items:
        medicine_name, quantity, total_item = item
        pdf.cell(0, 10, text=f'Medicine: {medicine_name}\n Quantity: {quantity}\n Total: {total_item}', 
                new_x='LMARGIN', new_y='NEXT', align='L')
    pdf.cell(0, 10, text='Total Amount: ' + str(calculate_total()),
            new_x='LMARGIN', new_y='NEXT', align='L')
    pdf.output('invoice.pdf')

# Medicine Selection Frame
medicine_frame = Frame(root, bg='#f7f9fc')
medicine_frame.grid(row=0, column=0, columnspan=2, pady=(20, 10), padx=20, sticky='w')

Label(medicine_frame, text='Select Medicine:', font=font_main, bg='#f7f9fc', fg='#2c3e50').grid(row=0, column=0, sticky='w')
medicine_listbox = Listbox(medicine_frame, selectmode=SINGLE, font=font_main, bg='white', fg='#2c3e50', bd=1, relief='solid', height=6)
medicine_listbox.grid(row=1, column=0, pady=5)
for medicine in medicines:
    medicine_listbox.insert(END, medicine)

Label(medicine_frame, text='Quantity:', font=font_main, bg='#f7f9fc', fg='#2c3e50').grid(row=0, column=1, padx=(20, 0), sticky='w')
qty_entry = Entry(medicine_frame, font=font_main, bg='white', fg='#2c3e50', bd=1, relief='solid', width=10)
qty_entry.grid(row=1, column=1, padx=(20, 0), pady=5)

add_btn = Button(medicine_frame, text='Add Medicine', font=font_main, bg='#3498db', fg='white', activebackground='#2980b9', command=add_medicine)
add_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Invoice Summary Frame
summary_frame = Frame(root, bg='#f7f9fc')
summary_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky='w')

Label(summary_frame, text='Total Amount:', font=font_main, bg='#f7f9fc', fg='#2c3e50').grid(row=0, column=0, sticky='w')
total_amt_entry = Entry(summary_frame, font=font_main, bg='white', fg='#2c3e50', bd=1, relief='solid', width=20)
total_amt_entry.grid(row=0, column=1, padx=10, pady=5)

Label(summary_frame, text='Customer Name:', font=font_main, bg='#f7f9fc', fg='#2c3e50').grid(row=1, column=0, sticky='w')
customer_entry = Entry(summary_frame, font=font_main, bg='white', fg='#2c3e50', bd=1, relief='solid', width=20)
customer_entry.grid(row=1, column=1, padx=10, pady=5)

generate_invoice_btn = Button(summary_frame, text='Generate Invoice', font=font_main, bg='#27ae60', fg='white', activebackground='#1e8449', command=generate_invoice)
generate_invoice_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Invoice Text Display
invoice_text = Text(root, height=10, width=60, font=font_main, bg='white', fg='#2c3e50', bd=1, relief='solid')
invoice_text.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

# Footer
footer = Label(root, text="© 2025 PhilipsTech | PDF Invoice Generator", font=("Segoe UI", 9), bg="#f7f9fc", fg="#888")
footer.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

