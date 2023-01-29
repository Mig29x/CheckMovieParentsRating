import PyPDF2

# Abrir el archivo PDF
with open('example.pdf', 'rb') as file:
    # Crear un objeto PDF
    pdf = PyPDF2.PdfFileReader(file)

    # Iterar sobre todas las páginas
    for page in range(pdf.getNumPages()):
        # Obtener el texto de la página actual
        text = pdf.getPage(page).extractText()
        print(text)
