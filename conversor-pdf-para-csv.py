# restrições do programa: tenha somente na pasta os arquivos pdfs! Além disso, não coloque, no nome dos arquivos um ".", deixe somente o "." do ".pdf"

from os import chdir, getcwd, listdir
import tabula

cam = input('Digite o caminho: ')

chdir(cam)
print(getcwd())

lista = []  # lista em pdf
lista2 = []  # lista em csv

for c in listdir():  # coleta o nome de todos os arquivos da pasta para a lista
    lista.append(c)

lista2 = lista[
         :]  # pega os mesmos arquivos de uma lista e passa para outra, assim podemos mudar o "final" do nome do arquivo (.pdf para .csv)

for i in range(0,
               len(lista2)):  # for com o intuito de tirar o ".pdf" e colocar ".csv" para poder exercutar no método final
    mudar = lista2[i].find(".pdf")
    nova_palavra = lista2[i][:mudar] + "_convertido"
    nova_palavra = nova_palavra + ".csv"
    lista2[i] = nova_palavra

print(lista)  # printa da lista em pdf
print(lista2)  # print da lista em csv

for i in range(0, len(lista2)):  # conversão de cada lista na pasta de pdf para csv
    print(lista[i])  # arquivo que será convertido
    print(lista2[i])  # arquivo convertido
    tabula.convert_into(lista[i], lista2[i], output_format="csv", pages='all')  # conversão