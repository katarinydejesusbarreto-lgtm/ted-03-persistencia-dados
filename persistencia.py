
import csv
import json
from pathlib import Path
from datetime import datetime
import shutil


PASTA_DADOS = Path(__file__).resolve().parent / 'dados'
ARQUIVO_CSV = PASTA_DADOS / 'livros.csv'
PASTA_BACKUPS = Path(__file__).resolve().parent / 'backups'


def criar_backup(caminho_arquivo):
    if not caminho_arquivo.exists():
        return True

    try:
        PASTA_BACKUPS.mkdir(parents=True, exist_ok=True)

        data_hora = datetime.now().strftime('%Y%m%d_%H%M%S')
        nome_backup = (
            f'{caminho_arquivo.stem}_'
            f'{data_hora}{caminho_arquivo.suffix}'
        )
        caminho_backup = PASTA_BACKUPS / nome_backup

        with open(caminho_arquivo, 'rb') as original:
            with open(caminho_backup, 'wb') as copia:
                shutil.copyfileobj(original, copia)

        print(f'Backup criado com sucesso: {nome_backup}')
        return True

    except OSError as erro:
        print(f'Erro ao criar backup: {erro}')
        return False


def ler_livros_csv():
    try:
        with open(ARQUIVO_CSV,mode='r',newline='',encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo,delimiter=';')
            livros = list(leitor)
            return livros

    except FileNotFoundError:
        print('Erro: o arquivo livros.csv não foi encontrado.')

    except PermissionError:
        print('Erro: você não tem permissão para ler o arquivo.')

    except UnicodeDecodeError:
        print('Erro: não foi possível interpretar a codificação do arquivo.')

    except OSError as erro:
        print(f'Erro ao ler o arquivo: {erro}')

    return []


def converter_csv_para_json():
    livros = ler_livros_csv()

    if not livros:
        print('Não há livros para converter.')
        return

    arquivo_json= PASTA_DADOS/'livros.json'
    if not criar_backup(arquivo_json):
        print('Conversão cancelada para preservar dados.')
        return

    try:
        with open(PASTA_DADOS / 'livros.json',mode='w',encoding='utf-8') as arquivo:
            json.dump(livros,arquivo,ensure_ascii=False,indent=4)

        print('Conversão de CSV para JSON realizada com sucesso.')

    except PermissionError:
        print('Erro: você não tem permissão para escrever no arquivo JSON.')

    except OSError as erro:
        print(f'Erro ao salvar o arquivo JSON: {erro}')


def converter_json_para_csv():
    arquivo_json = PASTA_DADOS / 'livros.json'
    arquivo_csv = PASTA_DADOS / 'livros_convertidos.csv'

    try:
        with open(arquivo_json,mode='r',encoding='utf-8') as arquivo:
            livros = json.load(arquivo)

        if not isinstance(livros, list):
            print('Erro: o JSON deve conter uma lista de livros.')
            return

        if not livros:
            print('Não há livros para converter.')
            return

        if not all(isinstance(livro, dict) for livro in livros):
            print('Erro: os dados do JSON estão em formato inválido.')
            return

        if not criar_backup(arquivo_csv):
            print('Conversão cancelada para preservar os dados.')
            return

        with open(arquivo_csv,mode='w',newline='',encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo,fieldnames=livros[0].keys())
            escritor.writeheader()
            escritor.writerows(livros)

        print('Conversão de JSON para CSV realizada com sucesso.')

    except FileNotFoundError:
        print('Erro: o arquivo livros.json não foi encontrado.')

    except UnicodeDecodeError:
        print('Erro: não foi possível interpretar a codificação do arquivo JSON.')

    except json.JSONDecodeError:
        print('Erro: o arquivo JSON não contém dados válidos.')

    except PermissionError:
        print('Erro: você não tem permissão para acessar o arquivo.')

    except OSError as erro:
        print(f'Erro ao trabalhar com os arquivos: {erro}')
