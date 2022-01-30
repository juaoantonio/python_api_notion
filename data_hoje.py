from datetime import datetime


def hoje():
    dia_semana = {
        'Mon': 'Segunda-Feira',
        'Tue': 'Terça-Feira',
        'Wed': 'Quarta-Feira',
        'Thu': 'Quinta-Feira',
        'Fri': 'Sexta-Feira',
        'Sat': 'Sábado',
    }

    try:
        dia = dia_semana[f"{datetime.today().strftime('%a')}"]

    except KeyError:
        raise Exception('Hoje é Domingo, então, não temos relatorio!')

    return dia
