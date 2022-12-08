import PyPDF2 as pdf
import sys

def error(msg: str):
    print(msg, file=sys.stderr)

def merge(files: list[str], outfile: str):
    merger = pdf.PdfFileMerger()
    for file in files:
        try:
            merger.append(file)
        except FileNotFoundError:
            error(f'Could not find file: {file} - Skipping!')
    
    with open(outfile, 'wb') as f:
        merger.write(f)

if __name__ == "__main__":
    while(True):
        print("Enter paths, to stop write !all (!exit to exit):")
        paths = []
        is_all = False
        
        while(not is_all):
            path = input()
            if(path == "!all"):
                is_all = True
                continue

            if(path == "!exit"):
                exit(0)

            paths.append(path)
        
        print("Enter new path (leave blank for ./merged.pdf):")
        new = input()
        if(new == ""):
            new = "merged.pdf"

        merge(paths, new)