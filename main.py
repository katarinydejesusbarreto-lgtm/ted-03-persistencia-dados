from persistencia import converter_csv_para_json,converter_json_para_csv

while True:
    print('\n===SISTEMA DE BIBLIOTECA==')
    print('1 - Converter CSV para JSON')
    print('2 - Converter JSON para CSV')
    print('0 - Sair')

    opcao= input('Escolha uam opção: ')

    if opcao == '1':
        converter_csv_para_json()

    elif opcao == '2':
        converter_json_para_csv()

    elif opcao == '0':
        print('Encerrando o programa...')
        break

    else:
        print('Opção Inválida.Tente Novamente.')