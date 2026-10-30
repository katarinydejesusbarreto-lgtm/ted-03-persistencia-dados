# TED 03 — Gerenciador de Persistência de Dados em Arquivos Estruturados (CSV e JSON)

## 1. Identificação

**Instituição:** UniBalsas  
**Curso:** Análise e Desenvolvimento de Sistemas (ADS)  
**Disciplina:** Algoritmos e Programação Avançada 
**Integrantes:**  
- Ana Clara Ribeiro Quixabeira 
- Katariny de Jesus Barreto

## 2. Descrição do projeto

O projeto consiste no desenvolvimento de um sistema em Python para trabalhar com persistência de dados em arquivos estruturados nos formatos CSV e JSON. O sistema utiliza dados de livros de uma biblioteca para demonstrar a leitura de arquivos, a conversão entre formatos e a criação de cópias de segurança.

O objetivo é preservar os dados durante as operações, organizar o código em funções e tratar possíveis erros durante o acesso aos arquivos.

## 3. Funcionalidades

O sistema apresenta as seguintes funcionalidades:

- Leitura de registros de livros armazenados em um arquivo CSV.
- Conversão dos dados de CSV para JSON.
- Conversão dos dados de JSON para CSV.
- Criação automática de backups antes de sobrescrever arquivos de destino existentes.
- Tratamento de erros relacionados à leitura, à escrita e ao acesso aos arquivos.
- Validação básica da estrutura dos dados JSON antes da conversão para CSV.
- Testes automatizados para verificar a leitura, as conversões, o tratamento de arquivo inexistente e a criação de backup.

## 4. Organização dos arquivos

O projeto está organizado da seguinte maneira:

```text
ted-03-persistencia-dados/
├── backups/
├── dados/
│   ├── livros.csv
│   ├── livros.json
│   └── livros_convertidos.csv
├── testes/
│   └── testar_persistencia.py
├── main.py
├── persistencia.py
├── README.md
└── .gitignore
```

A pasta `dados` armazena os arquivos utilizados pelo sistema. A pasta `backups` guarda cópias de segurança, enquanto a pasta `testes` contém os testes automatizados.

O arquivo `main.py` apresenta o menu de opções, e o arquivo `persistencia.py` contém as funções responsáveis pelas operações com os arquivos.

## 5. Tecnologias utilizadas

- Python 3
- Módulo `csv`
- Módulo `json`
- Módulo `pathlib`
- Módulo `datetime`
- Módulo `shutil`
- Módulo `unittest`

## 6. Como executar o sistema

**Pré-requisito:** ter o Python instalado e o projeto aberto no Visual Studio Code ou em outro terminal.

1. Abra o terminal na pasta principal do projeto.
2. Execute o comando:

```bash
python main.py
```

3. Escolha uma das opções apresentadas no menu:

- `1` — Converter CSV para JSON.
- `2` — Converter JSON para CSV.
- `0` — Encerrar o sistema.

## 7. Como executar os testes

Com o terminal aberto na pasta principal do projeto, execute:

```bash
python -m unittest testes.testar_persistencia -v
```

Os testes verificam a leitura do CSV, o tratamento de arquivo inexistente, a conversão de CSV para JSON, a conversão de JSON para CSV e a preservação do conteúdo original no backup.

Na execução realizada durante o desenvolvimento, os cinco testes foram aprovados, com o resultado `OK`.

## 8. Tratamento de erros e segurança dos dados

O código utiliza a estrutura `with open()` para abrir arquivos e garantir o fechamento automático dos recursos após as operações. Também especifica a codificação UTF-8 nas operações de leitura e escrita de texto.

O sistema trata situações como arquivo inexistente, falta de permissão, falhas de codificação, JSON inválido e outros erros de entrada e saída.

Antes de sobrescrever um arquivo de destino existente, a função de backup cria uma cópia de segurança. Dessa forma, uma versão anterior pode ser preservada caso seja necessário recuperá-la.

## 9. Considerações finais

O desenvolvimento do projeto permitiu aplicar conceitos de persistência de dados em arquivos estruturados, manipulação de CSV e JSON, tratamento de exceções, organização de código em funções e testes automatizados.

As conversões foram verificadas por meio de testes, buscando garantir que os registros dos livros fossem preservados durante a mudança entre os formatos. A implementação de backups também contribui para a proteção dos dados durante as operações de escrita.
