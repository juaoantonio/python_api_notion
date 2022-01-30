import requests
import os
import json_manipulator


def pegar_id_database(token, page_id, dia_atual):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("GET", url, headers=headers)
    dados = response.json()

    blocks = dados['results']

    bases_de_dados = dict()
    for block in range(len(blocks)):
        try:
            block_id = blocks[block]['id']
            block_title = blocks[block]['child_database']['title']
            bases_de_dados[f'{block_title}'] = block_id

        except KeyError:
            pass

    database_id = bases_de_dados[f"{dia_atual}"]

    return database_id


def pegar_nome_vendedor(token, page_id):
    url = f"https://api.notion.com/v1/pages/{page_id}/properties/title"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()

    nome_vendedor = data['results'][0]['title']['plain_text']

    return nome_vendedor


def database_para_csv(token, database_id, nome_vendedor):
    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    payload = {"page_size": 100}

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    data = response.json()

    if not os.path.isdir('dados'):
        os.mkdir('dados')

    json_manipulator.to_csv(data, f'dados/{nome_vendedor}.csv')
