import Pyro5.api

math_obj = Pyro5.api.Proxy("PYRONAME:example.math")
greeting_obj = Pyro5.api.Proxy("PYRONAME:example.greeting")
print('funções do servidor:\n- greetings\n- sum\n- multip')

while True:
    try:
        function_call = input(':')
        if function_call == 'exit': raise KeyboardInterrupt

        elif function_call == 'greetings': 
            name = input('What is your name? ')
            print(greeting_obj.get_fortune(name))

        elif function_call == 'sum':
            valores = input('digite os valores a serem somados\n:').split(' ')
            valores = list(map(lambda x: int(x),valores))
            print(math_obj.sum(valores))

        elif function_call == 'multip':
            valores = input('digite os valores a serem multiplicados\n:').split(' ')
            valores = list(map(lambda x: int(x),valores))
            print(math_obj.mult(valores))

        else:
            raise ModuleNotFoundError

    except KeyboardInterrupt:
        print("finalizando programa:")
        break
    except ModuleNotFoundError:
        print(f'nenhum módulo com nome de {function_call}')
    except Exception as e:
        print(e)