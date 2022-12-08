import merge.pdf_merge as pm
import split.pdf_split as sp
import PyPDF2 as pdf
import sys

def error(msg: str):
    print(msg, file=sys.stderr)

if __name__ == "__main__":
    arg = sys.argv
    if(len(arg) < 2):
        error("No Argument")
        sys.exit(1)
    
    if(arg[1] == "-m"):
        if(len(arg) < 5):
            error("Too few arguments")
            sys.exit(1)

        paths = []
        for i in range(3, len(arg)):
            print(arg[i])
            paths.append(arg[i])

        pm.merge(paths, arg[2])
        sys.exit(0)
    elif(arg[1] == "-s"):
        if(len(arg) != 3):
            error("Invalid Argument")
            sys.exit(1)
        
        root = arg[2].split()
        path = ""
        for i in range(0, len(root)-1):
            path += f'{root[i]}/'
        
        try:
            reader = pdf.PdfFileReader(arg[2])
            sp.split(path, "Page_", reader)
        except FileNotFoundError:
            error("File not found")
            sys.exit(1)
        sys.exit(0)
    else:
        error("Unknown Argument")
        sys.exit(1)