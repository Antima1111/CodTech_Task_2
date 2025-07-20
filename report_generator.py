import pandas as pd
from fpdf import FPDF

df = pd.read_csv("sales_data.csv")

total = df["Sales"].sum()
top = df.loc[df["Sales"].idxmax()]

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')

pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(200, 10, txt=f"Total Sales: {total}", ln=True)
pdf.cell(200, 10, txt=f"Top Product: {top['Product']} - {top['Sales']} units", ln=True)

pdf.ln(10)
pdf.cell(50, 10, "Product", 1)
pdf.cell(50, 10, "Sales", 1)
pdf.ln()
for i, row in df.iterrows():
    pdf.cell(50, 10, row["Product"], 1)
    pdf.cell(50, 10, str(row["Sales"]), 1)
    pdf.ln()

pdf.output("sales_report.pdf")
print("Your Report is Ready!")