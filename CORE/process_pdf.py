from pdf_reader import extract_text_from_pdf

pdf_text = extract_text_from_pdf(
    "UPLOADS/DAY 3 REPORT.pdf"
)

with open(
    "DATA/uploaded_pdf.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(pdf_text)

print("PDF text saved successfully!")