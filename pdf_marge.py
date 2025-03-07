from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["I130A.pdf", "N-565.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
