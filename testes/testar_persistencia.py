import csv
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
import persistencia

from persistencia import ler_livros_csv


class TestarPersistencia(unittest.TestCase):

    def test_leitura_csv(self):
        livros = ler_livros_csv()

        self.assertEqual(len(livros), 5)
        self.assertIn('titulo', livros[0])
        self.assertIn('autor', livros[0])

    def test_csv_nao_encontrado(self):
        caminho_falso = Path('arquivo_inexistente.csv')

        with patch.object(persistencia, 'ARQUIVO_CSV', caminho_falso):
            with patch('builtins.print') as mensagem:
                livros = ler_livros_csv()

        self.assertEqual(livros, [])
        mensagem.assert_called_once_with(
            'Erro: o arquivo livros.csv não foi encontrado.'
        )
    
    def test_conversao_csv_para_json(self):
        livros_teste = [
            {
                'id': '1',
                'titulo': 'Livro de Teste',
                'autor': 'Autora Teste',
                'genero': 'Fantasia',
                'ano': '2025'
            }
        ]

        with tempfile.TemporaryDirectory() as pasta:
            pasta_teste = Path(pasta)
            arquivo_csv_original = persistencia.ARQUIVO_CSV
            pasta_dados_original = persistencia.PASTA_DADOS

            try:
                persistencia.PASTA_DADOS = pasta_teste
                persistencia.ARQUIVO_CSV = pasta_teste / 'livros.csv'

                with open(persistencia.ARQUIVO_CSV,'w',newline='',encoding='utf-8') as arquivo:
                    escritor = csv.DictWriter(arquivo,fieldnames=livros_teste[0].keys(),delimiter=';')
                    escritor.writeheader()
                    escritor.writerows(livros_teste)

                persistencia.converter_csv_para_json()

                arquivo_json = pasta_teste / 'livros.json'

                with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
                    livros_convertidos = json.load(arquivo)

                self.assertEqual(livros_convertidos, livros_teste)

            finally:
                persistencia.ARQUIVO_CSV = arquivo_csv_original
                persistencia.PASTA_DADOS = pasta_dados_original
    
    def test_conversao_json_para_csv(self):
        livros_teste = [
            {
                'id': '1',
                'titulo': 'Livro de Teste',
                'autor': 'Autora Teste',
                'genero': 'Fantasia',
                'ano': '2025'
            }
        ]

        with tempfile.TemporaryDirectory() as pasta:
            pasta_teste = Path(pasta)
            arquivo_json = pasta_teste / 'livros.json'
            arquivo_csv_original = ( persistencia.PASTA_DADOS / 'livros_convertidos.csv')
            pasta_dados_original = persistencia.PASTA_DADOS

            try:
                persistencia.PASTA_DADOS = pasta_teste

                with open(arquivo_json,mode='w',encoding='utf-8') as arquivo:
                    json.dump(livros_teste, arquivo, ensure_ascii=False)

                persistencia.converter_json_para_csv()

                arquivo_csv = pasta_teste / 'livros_convertidos.csv'

                with open(arquivo_csv,mode='r',newline='',encoding='utf-8') as arquivo:
                    leitor = csv.DictReader(arquivo)
                    livros_convertidos = list(leitor)

                self.assertEqual(livros_convertidos, livros_teste)

            finally:
                persistencia.PASTA_DADOS = pasta_dados_original

    def test_criar_backup_preserva_arquivo_original(self):
        with tempfile.TemporaryDirectory() as pasta:
            pasta_teste = Path(pasta)

            arquivo_original = pasta_teste / 'livros.json'
            pasta_backups_original = persistencia.PASTA_BACKUPS

            try:
                persistencia.PASTA_BACKUPS = pasta_teste / 'backups'

                conteudo_antigo = '{"titulo": "Livro antigo"}'
                arquivo_original.write_text(conteudo_antigo,encoding='utf-8')

                resultado = persistencia.criar_backup(arquivo_original)

                self.assertTrue(resultado)

                arquivos_backup = list(persistencia.PASTA_BACKUPS.glob('livros_*.json'))

                self.assertEqual(len(arquivos_backup), 1)

                conteudo_backup = arquivos_backup[0].read_text(encoding='utf-8')

                self.assertEqual(conteudo_backup, conteudo_antigo)

            finally:
                persistencia.PASTA_BACKUPS = pasta_backups_original


if __name__ == '__main__':
    unittest.main()
