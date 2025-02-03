import os
from tkinter.filedialog import askdirectory

local= askdirectory(title= "Selecione a pasta")

lista_arq= os.listdir(local)

tipos_arq= {
    "ARQ Imagens": [".png", ".jpg"],
    "ARQ Planilhas": [".xlsx"],
    "ARQ PDFs": [".pdf"],
    "ARQ CSV": [".csv"] 
}

for arq in lista_arq:
    nome, extensao= os.path.splitext("{}/{}" .format(local, arq))
    for pasta in tipos_arq:
        if extensao in tipos_arq[pasta]:
            if not os.path.exists("{}/{}" .format(local, pasta)):
                os.mkdir("{}/{}" .format(local, pasta))
                os.rename("{}/{}" .format(local, arq), "{}/{}/{}" .format(local, pasta, arq))