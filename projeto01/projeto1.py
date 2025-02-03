import PyPDF2
import os

mesc= PyPDF2.PdfMerger()

lista_arq= os.listdir("relatórios")
lista_arq.sort()

for arq in lista_arq:
    if ".pdf" in arq:
        mesc.append("relatórios/{}" .format(arq))

mesc.write("Relatório_individuais.pdf")