import csv
import pandas as pd
from openpyxl import load_workbook


def writer_csv_excel(csv_path, excel_path, nome_planilha, nome_vendedor):
    file = open(csv_path)
    csvreader = csv.reader(file)
    r = 2
    c = int()

    rows = []
    for row in csvreader:
        rows.append(row)

    df = pd.DataFrame(rows)

    workbook = load_workbook(excel_path, data_only=True)
    sheet = workbook[nome_planilha]

    cell_column = {
        'A1': 0,
        'D1': 3,
        'G1': 6,
        'J1': 9,
    }

    for cell, column in cell_column.items():
        if nome_vendedor.lower() == str(sheet[cell].value).lower():
            c = column

    with pd.ExcelWriter(excel_path, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
        df.to_excel(writer, sheet_name="Dados", startrow=r, startcol=c, index=False, header=False)

