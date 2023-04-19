try:
    value = int(input('Entre com um numero: '))
    print('O valor: ', value, 'dividido por um é: ', 1/value)
except ValueError:
    print('Erro. Verifique o valor fornecido.')
except ZeroDivisionError:
    print('Não é possivel fazer a divisão por zero.')
except:
    print('Algo errado aconteceu!')