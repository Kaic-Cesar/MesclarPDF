import PyPDF2 
import os

merger = PyPDF2.PdfMerger()

# Informa o diretório onde contém os arquivos
lista_arquivos = os.listdir("arquivos") 

# Organiza os arquivos em ordem
lista_arquivos.sort() 
print(lista_arquivos)

# Fará um loop no diretório e pegará somente os arquivos com a extensão .pdf 
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}") # Acrescenta na variável 'merger' os arquivos que está no diretório e seja true com a condição
 
# Cria o novo arquvio .pdf 
merger.write("arquivos/PDF Final.pdf")
