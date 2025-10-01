# 💊 Invoice Generator (Tkinter + FPDF)

A sleek desktop application built with Python's Tkinter and FPDF libraries to generate PDF invoices for medicine purchases. Designed with a modern UI and intuitive workflow, this tool is perfect for pharmacies, clinics, or small businesses managing medicine sales.

---

## 🖼️ Features

- 🧾 Add medicines with quantity and auto-calculated totals
- 🧍 Input customer name for personalized invoices
- 📄 Generate clean, printable PDF invoices
- 💅 Stylish, modern UI with custom fonts and colors
- 🖥️ Desktop-friendly layout using Tkinter grid system

---

## 📦 Requirements

- Python 3.7+
- `fpdf` library

Install dependencies:

```bash
pip install fpdf
```

🚀 How to Run
```bash
python invoice_generator.py
```
Make sure the `images/photo.ico` file exists for the window icon. You can replace it with your own `.ico` file.

🧪 Sample Medicines
The app includes a predefined list of medicines with prices:

```code
medicines = {
    'Medicine A': 10,
    'Medicine B': 20,
    'Medicine C': 15,
    'Medicine D': 35,
    'Medicine E': 15,
    'Medicine F': 45,
    'Medicine G': 26,
}
```
You can customize this dictionary to suit your inventory.

🧠 How It Works
1. Select a medicine from the list.
2. Enter the quantity and click Add Medicine.
3. Enter the customer's name.
4. Click Generate Invoice to create a PDF file named invoice.pdf.

The invoice includes:
- Customer name
- List of medicines with quantity and total
- Grand total amount

📁 Output
The generated invoice is saved as:

```Code
invoice.pdf
```
You’ll find it in the same directory as the script.

🖌️ UI Design Highlights
- Flat design with soft background (#f7f9fc) and accent colors
- Segoe UI font for clean readability
- Grid layout for structured alignment
- Button hover effects and styled widgets
- Footer branding: © 2025 PhilipsTech | PDF Invoice Generator

  🛠️ Customization Tips
- 💼 Replace medicines dictionary with your own product list
- 🎨 Tweak colors and fonts to match your brand
- 📄 Extend PDF layout with logos, headers, or tables
- 🔒 Add validation for quantity and customer fields

📜 License
This project is licensed under the MIT License. Feel free to modify and distribute.

```code
Let me know if you’d like a logo badge, screenshots, or GitHub Actions setup for packaging this into an installer!
```
