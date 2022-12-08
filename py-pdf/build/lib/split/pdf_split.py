import PyPDF2 as pdf

def split(path:str, pattern: str, reader: pdf.PdfFileReader):
    pnr = 1
    for page in reader.pages:
        writer = pdf.PdfFileWriter()
        writer.add_page(page)
        with open(f'{path}{pattern}{pnr}.pdf', 'wb') as file:
            writer.write(file)
        pnr += 1


if __name__ == "__main__":
    print("PDF-Splitter:\n")
    path = ""
    while(True):
        print("Enter path to pdf (!exit to exit program):")
        path = input()
        
        if(path == "!exit"):
            exit(0)
        
        try:
            reader = pdf.PdfFileReader(path)
        except FileNotFoundError:
            print("File not found!")
            continue

        path_structure = path.split('/')
        root = ""
        for i in range(0, len(path_structure)-1):
            root += f'{path_structure[i]}/'
        print(f'Creating new PDFs in: {root}')
        split(root, "PAGE-", reader)