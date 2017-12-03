def debug_call(f, *args, **kwargs):
    """Wywołuje funkcję z danymi argumentami wypisując jej argumenty przed
    wywołaniem"""
    print("Wywołam funkcję: {}".format(f))
    print("Argumenty pozycyjne:")
    for arg in args:
        print('\t' + arg)
    print("Argumenty pozycyjne:")
    for k, v in kwargs.items():
        print('\t{}: {}'.format(k, v))
    f(*args, **kwargs)
