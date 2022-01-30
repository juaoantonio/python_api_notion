import json


def create_file(data, json_name):
    with open(json_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def to_csv(json_data, csv_name):
    # Carrega o arquivo
    obj = json_data

    # Escreve os dados num arquivo csv
    results = len(obj['results'])

    with open(csv_name, 'w') as csv_file:
        for i in range(results):
            cliente_do_dia = obj['results'][i]['properties']['CLIENTES DO DIA']['title']
            motivo_nao_venda = obj['results'][i]['properties']['MOTIVO DE NÃO VENDA']['multi_select']

            if not cliente_do_dia:
                cliente_motivo = ''

            elif motivo_nao_venda:
                cliente_motivo = f"{cliente_do_dia[0]['plain_text']}, {motivo_nao_venda[0]['name']}\n"

            else:
                cliente_motivo = f"{cliente_do_dia[0]['plain_text']},\n"

            csv_file.write(cliente_motivo)
