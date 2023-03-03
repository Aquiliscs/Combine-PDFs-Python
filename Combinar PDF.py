import os
from datetime import datetime
from PyPDF2 import PdfMerger

# diretório onde os arquivos PDF estão localizados
pdf_dir = 'C:/Temp/PDF'

# lista todos os arquivos PDF no diretório
pdf_files = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

# cria um objeto PdfFileMerger para combinar os arquivos PDF
merger = PdfMerger()

# adiciona cada arquivo PDF ao objeto PdfMerger
for pdf in pdf_files:
    merger.append(open(pdf, 'rb'))

# cria um nome de arquivo para o arquivo PDF combinado
filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.pdf'

# diretório onde o arquivo combinado será salvo
output_dir = 'C:/Temp'

# salva o arquivo PDF combinado com o nome de arquivo criado anteriormente
output_file = os.path.join(output_dir, filename)
with open(output_file, 'wb') as outfile:
    merger.write(outfile)

# fecha o objeto PdfMerger
merger.close()
