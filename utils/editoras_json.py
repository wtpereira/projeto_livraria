import json
from model.editora import Editora

# Página 26
def ler_json_pagina_26(nome_arquivo_json) -> list[dict]:
    with(open(nome_arquivo_json)) as arquivo_json:
        dados = json.load(arquivo_json)
        print(dados)


# Página 27
def ler_json(nome_arquivo_json) -> list[dict]:
    with(open(nome_arquivo_json)) as arquivo_json:
        dados = json.load(arquivo_json)

    return dados


# Página 28
def ler_json_e_gera_uma_lista_de_editoras(nome_arquivo_json) -> list[Editora]:
    with(open(nome_arquivo_json)) as arquivo_json:
        dados = json.load(arquivo_json)
        lista_editoras = list()
        for dicionario in dados:
            editora = Editora(dicionario['nome'], dicionario['endereco'], dicionario['telefone'])
            lista_editoras.append(editora)

    return lista_editoras


# Página 29
def criando_json_usando_lista_de_dict(lista_dict, nome_novo_arquivo) -> None:
    with open(nome_novo_arquivo, 'w' , newline='') as novo_arquivo:
        # Se ensure_ascii for verdadeiro (o padrão), será garantido que a saída terá todos os caracteres não ASCII que chegam escapados.
        # Se ensure_ascii for falso, a saída desses caracteres ficará como está.
        # Fonte: https://docs.python.org/pt-br/3/library/json.html#basic-usage
        json.dump(lista_dict, novo_arquivo, ensure_ascii=False, indent=4)

    print('Os dados foram salvos no novo arquivo!')



# Página 30
def criando_json_usando_lista_de_editoras(lista_editoras, nome_novo_arquivo) -> None:
    with open(nome_novo_arquivo, 'w' , newline='') as novo_arquivo:
        editoras_dict = list()
        for editora in lista_editoras:
            editoras_dict.append(editora.__dict__)

        json.dump(editoras_dict, novo_arquivo, ensure_ascii=False, indent=4)

    print('Os dados foram carregados com sucesso!')



# Página 31
def criando_json_usando_lista_de_editoras(lista_editoras, nome_novo_arquivo) -> None:
    with open(nome_novo_arquivo, 'w' , newline='') as novo_arquivo:
        editoras_dict = list()
        for editora in lista_editoras:
            editoras_dict.append(editora.as_dict())

        json.dump(editoras_dict, novo_arquivo, ensure_ascii=False, indent=4)

    print('Os dados foram carregados com sucesso!')


if __name__ == '__main__':
    # print(ler_json('editoras.json'))
    print(ler_json_e_gera_uma_lista_de_editoras('editoras.json'))
