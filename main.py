import notion
from decouple import config
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

# Token secreto de acesso do Notion
token_integracao = config('TOKEN')

# Pages ID de cada vendedor
pages_id = [
    '0d882d49b1ed496aab8f8cd10ec1e46f',
    '8aafbcc468fa485b883c3733f32e239c',
    '9d7f1709807b428fbaae507f8f1699a4',
    'f65132a722e04533b81c2cb358d3b36b',
]

for page_id in pages_id:
    nome_vendedor = notion.pegar_nome_vendedor(token_integracao, page_id)
    database_id = notion.pegar_id_database(token_integracao, page_id, dia_atual)

    notion.database_para_csv(token_integracao, database_id, nome_vendedor)
