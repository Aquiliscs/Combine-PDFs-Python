import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger, PdfReader

# seleciona a pasta de onde os arquivos PDF serão combinados
folder_selected = r'C:\Temp\PDF'

# cria um objeto de mesclagem de arquivos PDF
pdf_merger = PdfMerger()

# mescla todos os arquivos PDF na pasta selecionada
for filename in os.listdir(folder_selected):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(folder_selected, filename)
        pdf_merger.append(PdfReader(open(pdf_path, 'rb')))

# solicita ao usuário que escolha o nome do arquivo PDF resultante
root = tk.Tk()
root.withdraw()
result_filename = filedialog.asksaveasfilename(initialdir=r'C:\Temp', defaultextension='.pdf')

# salva o arquivo PDF resultante com o nome escolhido
with open(result_filename, 'wb') as output:
    pdf_merger.write(output)

print('Os arquivos PDF foram combinados com sucesso!')

#commit teste 2