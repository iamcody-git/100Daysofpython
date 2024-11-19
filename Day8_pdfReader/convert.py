import pdfplumber

# pip install PyPDF2 pdfplumber : first install this 

# Load the PDF file
pdf_path = "apply1.pdf"  
text = ""

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text()

# Save to a text file
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("PDF text extracted and saved to output.txt")
