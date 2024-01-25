from pdf2docx import Converter

def convert_pdf_to_docx(pdf_path, docx_path):
     # Convert PDF to Word
     cv = Converter(pdf_path)
     cv.convert(docx_path, start=0, end=None)
     cv.close()

# Example usage
pdf_file_path = 'file.pdf' #file to convert
docx_file_path = 'convertedfile.docx' #result file

convert_pdf_to_docx(pdf_file_path, docx_file_path)
