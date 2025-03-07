import PyPDF2

writer = PyPDF2.PdfWriter()

# Add pages to encrypt
with open('newdd.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

# Encrypt the PDF with a password
writer.encrypt('password123')

# Save the encrypted PDF
with open('encrypted.pdf', 'wb') as output_pdf:
    writer.write(output_pdf)