def main():
    soma_salario_anterior, soma_salario_novo, salario = 0, 0, 1.0
    while salario > 0:
        salario = float(input("digite o salario dos funcionarios: "))
        soma_salario_anterior = soma_salario_anterior + salario
        novo_salario = calcSalario(salario)
        soma_salario_novo = soma_salario_novo + novo_salario
        print("Novo Salario R$ %2.f"%novo_salario)
    diferenca_salarios = soma_salario_novo - soma_salario_anterior
    print("Soma dos Novos Salarios R$ %2.f" % soma_salario_novo)
    print("Dieferenca das somas dos novos Salario R$ %2.f" % diferenca_salarios)

def calcSalario(valor):
    if valor < 3000.0:
        salario = valor + valor * 0.25
    if valor >= 3000.0 and valor < 6000.0:
        salario = valor + valor * 0.20
    if valor >= 6000.0 and valor < 10000.0:
        salario = valor + valor * 0.15
    if valor >= 10000.0:
        salario = valor + valor*0.10
    salario_reajustado = salario
    return salario_reajustado
if __name__=="__main__":
    main()