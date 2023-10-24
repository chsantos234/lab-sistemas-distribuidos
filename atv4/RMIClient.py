#import itertools
import Pyro5.api
import inspect


print("Classes:\n- greeting\n- math")

while True:
    object_to_use = input("Qual classe a ser usada? ")
    try:
        if object_to_use == 'exit': raise KeyboardInterrupt

        object_call = Pyro5.api.Proxy("PYRONAME:example."+ object_to_use)
        

        attrs = (getattr(object_call, name) for name in dir(object_call))
        methods = filter(inspect.ismethod, attrs)

        for method in methods:
            value = method()
            print(value)

    except KeyboardInterrupt:
        print("finalizando programa:")
        break
    #except Exception as e:
    #    print(e)