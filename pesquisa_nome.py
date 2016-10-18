#importa requisitos
import glob
import unittest
from unicodedata import normalize	

def remove_diacritic(s):
	return (normalize('NFKD', s)
			.encode('ascii', 'ignore')
			.decode('ascii'))


def pesquisa(fuzileiro=""):

    #listar todos txt
    todos_arqs = glob.glob('./**/*.txt',recursive=True)

    #declaracao de variavel
    arqs_encontrados = []

    #laço condicional
    for nome_do_arq_da_vez in todos_arqs:
        #abre o arquivo para memoria
        obj_arquivo_aberto = open(nome_do_arq_da_vez)


        #lista todas as linhas
        lista_de_linhas = obj_arquivo_aberto.readlines()
               
        #junta todas as linhas em um só string
        todas_as_linhas = remove_diacritic(' '.join(lista_de_linhas).lower())

        #desvio convencional
        if fuzileiro in todas_as_linhas:
            arqs_encontrados.append(nome_do_arq_da_vez)

    #saida de missoes
    return arqs_encontrados


if __name__ == '__main__':
    fuzileiro = remove_diacritic(input("Digite o nome do fuzileiro: ").lower())
    retorno_pesquisa = pesquisa(fuzileiro)
    print(retorno_pesquisa)








