import csv

from model.editora import Editora


# Página 06
def ler_csv_pagina_06() -> list:
    arquivo_csv = open('editoras.csv')
    csv_reader = csv.reader(arquivo_csv, delimiter=',')
    for linha in csv_reader:
        print(linha)


def ler_csv_pagina_07() -> list:
    lista_csv = list()
    with open('editoras.csv') as arquivo_csv:
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        primeira_linha = True
        for linha in csv_reader:
            lista_csv.append(linha)
            print(linha)


# Página 08
def ler_csv() -> list:
    lista_csv = list()
    with open('editoras.csv') as arquivo_csv:
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        primeira_linha = True
        for linha in csv_reader:
            lista_csv.append(linha)

    return lista_csv


# Página 09
def ler_csv_e_criando_uma_lista() -> list:
    with open('editoras.csv') as arquivo_csv:
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        lista_csv = list(csv_reader)
        return lista_csv


# Página 10
def ler_csv_e_criando_uma_lista_de_editoras() -> list:
    list_dict_csv = list()
    with open('editoras.csv') as arquivo_csv:
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        lista_csv = list(csv_reader)

        ignore_proxima_linha = True  # A primeira linha contém somente os títulos das colunas
        lista_editoras = list()
        for item in lista_csv:
            if ignore_proxima_linha:
                ignore_proxima_linha = False
            else:
                editora = Editora(item[0], item[1], item[2])
                lista_editoras.append(editora)


# Página 11
def ler_csv_e_gera_uma_lista_de_dict() -> list[dict]:
    list_dict_csv = list()
    with open('editoras.csv') as arquivo_csv:
        csv_reader = csv.DictReader(arquivo_csv, delimiter=',')
        for dicionario in csv_reader:
            list_dict_csv.append(dicionario)

    return list_dict_csv


# Página 12
def ler_csv_e_gera_uma_lista_de_editoras(nome_arquivo_csv) -> list[Editora]:
    lista_editoras = list()
    with open(nome_arquivo_csv) as arquivo_csv:
        csv_reader = csv.DictReader(arquivo_csv, delimiter=',')
        for dicionario in csv_reader:
            editora = Editora(dicionario['nome'], dicionario['endereço'], dicionario['telefone'])
            lista_editoras.append(editora)

    return lista_editoras


# Página 13
def criando_csv_usando_lista(lista) -> None:
    with open('novo_editoras.csv', 'w', newline='') as novo_arquivo:
        escritor = csv.writer(novo_arquivo)
        escritor.writerow(lista[0])
        escritor.writerow(lista[1:])
        print('Os dados foram carregados com sucesso!')



# Página 14
def criando_csv_usando_lista_de_editoras_pagina_14(lista_editoras) -> None:
    with open('novo_editoras.csv', 'w', newline='') as novo_arquivo:
        escritor = csv.writer(novo_arquivo)
        for editora in lista_editoras:
            escritor.writerow([editora.nome, editora.endereco, editora.telefone])

    print('Os dados foram carregados com sucesso!')


# Página 15
def criando_csv_usando_lista_de_editoras(lista_editoras: list[Editora], nome_arquivo_csv: str) -> None:
    with open(nome_arquivo_csv, 'w', newline='') as novo_arquivo:
        escritor = csv.writer(novo_arquivo)
        escritor.writerow(['nome', 'endereço', 'telefone'])
        for editora in lista_editoras:
            escritor.writerow([editora.nome, editora.endereco, editora.telefone])

    print('Os dados foram carregados com sucesso!')
