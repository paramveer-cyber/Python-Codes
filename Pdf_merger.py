import PyPDF2

try:
    counter = int(input("Please enter the Number of pdfs: "))
    pdfmerge = PyPDF2.PdfMerger()
    for i in range(counter):
        pdf_name = str(input("Enter the name of the pdf: "))
        pdfmerge.append(open(f"{pdf_name}.pdf", "rb"))
    file = open("output.pdf", "wb")
    pdfmerge.write(file)
    print("Done!")
except:
    print("Error Occured!, Please ensure that you have enter correct values.")