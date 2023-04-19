while True:
    try:
        numero = int(input('Entre com um número: '))
        print(5/numero)
        break
    except (ValueError, ZeroDivisionError):
        print('Desculpe, não posso dividir por zero.')
    except:
        print('Não sei oque fazer...')