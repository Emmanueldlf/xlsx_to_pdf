import pandas as pd
import glob
import openpyxl
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
# print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nb = filename.split("-")[0]
    date = invoice_nb = filename.split("-")[1]
    #invoice_nb, date = invoice_nb = filename.split("-")


    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nb.{invoice_nb}")



    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nb.{date}")

    pdf.output(f"pdfs/{filename}.pdf")
