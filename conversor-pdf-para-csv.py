# Restrições do programa: Não coloque, no nome dos arquivos um ".", deixe somente o "." do ".pdf"

from os import chdir, getcwd, listdir
import tabula

class Conversor:

    def __init__(self,diretorio: str) -> None:
        self.lista_pdf = []
        self.lista_csv = []
        self.diretorio = diretorio
    def converter(self) -> None:
        self.__lista_arquivos_pdf()
        self.__lista_arquivos_clv()
        self.__realizar_conversao()
    def __lista_arquivos_pdf(self) -> list:  #Método para definir todos os arquivos .pdf que serão convertidos da pasta
        chdir(self.diretorio)
        print("\nConvertendo arquivos .pdf do diretório {}\n------------------------------------------------------\n".format(getcwd()))

        for c in listdir():  # coleta o nome de todos os arquivos da pasta para a lista
            self.lista_pdf.append(c)
        self.lista_pdf = list(filter(lambda lista: '.pdf' in lista, self.lista_pdf))  # filtra somente os arquivos .pdf
    def __lista_arquivos_clv(self) -> list: #Método para obter o novo nome dos arquivos convertidos para .csv

        self.lista_csv = self.lista_pdf[:]

        for i in range(0, len(self.lista_csv)):  # for com o intuito de tirar o ".pdf" e colocar ".csv" para poder exercutar no método final
            mudar = self.lista_csv[i].find(".pdf")
            nova_palavra = self.lista_csv[i][:mudar] + "_convertido.csv"
            self.lista_csv[i] = nova_palavra
    def __realizar_conversao(self) -> None:  #Realiza a conversão final
        for i in range(0, len(self.lista_csv)):  # conversão de cada lista na pasta de pdf para csv
            print(self.lista_pdf[i])  # arquivo que será convertido
            tabula.convert_into(self.lista_pdf[i], self.lista_csv[i], output_format="csv", pages='all')  # conversão
            print("{}\n-------------------------".format(self.lista_csv[i]))  # arquivo convertido

diretorio = input('Digite o caminho da pasta: ')
run = Conversor(diretorio)
run.converter()
print("Conversão finalizada!")


