'''

def tabuada(valor, multiplicado_por):
    for i in range(10 - (multiplicado_por - 1)):
        print('{} x {} = {}'.format(valor, (multiplicado_por + i), (valor * (multiplicado_por + i))))
tabuada(6,3)

'''