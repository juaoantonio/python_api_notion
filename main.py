import json
import os
import notion
import csv_manipulator
from tkinter import filedialog
from data_hoje import hoje

# Armazena o dia presente por padrão, mas pode configurar com o dia que quiser, basta copiar na váriavel dia_atual
# um dos dias listados (com execeção do Domingo):
# 'Segunda-Feira'
# 'Terça-Feira'
# 'Quarta-Feira'
# 'Quinta-Feira'
# 'Sexta-Feira'
# 'Sábado'
dia_atual = hoje()

if not os.path.isfile('settings.json'):
    excel_path = filedialog.askopenfilename()

    config = {
        'excel_path': excel_path,
        'token': 'secret_TG7Xp8dj3VsNcm2FMskZFlzEdvJMmvoOMXmt81OGk42'
    }

    json_object = json.dumps(config, indent=4)
    with open('settings.json', 'w') as outfile:
        outfile.write(json_object)

with open('settings.json', 'r') as json_file:
    valores = json.load(json_file)

# Caminho da planilha de análises
excel_path = valores['excel_path']

# Token secreto de acesso do Notion
token_integracao = valores['token']

# Pages ID de cada vendedor
pages_id = [
    '0d882d49b1ed496aab8f8cd10ec1e46f',
    '8aafbcc468fa485b883c3733f32e239c',
    '9d7f1709807b428fbaae507f8f1699a4',
    'f65132a722e04533b81c2cb358d3b36b',
]

# Cria os arquivos em csv de cada base de dados do dia escolhido de cada vendedor
for page_id in pages_id:
    nome_vendedor = notion.pegar_nome_vendedor(token_integracao, page_id)
    database_id = notion.pegar_id_database(token_integracao, page_id, dia_atual)

    notion.database_para_csv(token_integracao, database_id, nome_vendedor)

    csv_manipulator.writer_csv_excel(f'dados/{nome_vendedor}.csv', excel_path, 'Dados', nome_vendedor)
