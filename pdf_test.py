from fpdf import FPDF
pdf = FPDF("P", "mm", "Letter")

pdf.add_page()

pdf.set_font('helvetica', '', 16)

pdf.cell(40,10, "Hello World")
pdf.cell(100,100, "Bye World")
pdf.image("Logo.png", 30, 30, 10)




pdf.output("pdf_1.pdf")