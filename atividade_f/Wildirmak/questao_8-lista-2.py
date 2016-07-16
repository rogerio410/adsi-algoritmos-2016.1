# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:32:26 2016

@author: Rubens
"""

def main():
    valor_hora = input('digite o valor da hora: ')
    qtd_hora = input('digite a quantidade de horas trabalhadas: ')
    sal = valor_hora * qtd_hora
    sind = 0.03*sal
    inss = 0.1*sal
    fgts = 0.11*sal
    print 'o salario bruto eh %d' %(sal)
    print 'o valor do sindicato eh %.2f e o valor do inss eh %.2f eo valor do fgts eh %.2f' %(sind, inss, fgts)
    if sal <= 900:
        sal_liquido = sal - (inss+sind)
        print 'salario liquido eh %.2f' %(sal_liquido)
        print 'o valor do fgts eh %.2f' %(fgts)
    elif sal > 900 and sal <= 1500:
        ir = 0.05*sal
        sal_liquido = sal - (inss+sind+ir)
        print 'salario liquido eh %.2f' %(sal_liquido)
        print 'o valor do fgts eh %.2f' %(fgts)
    elif sal > 1500 and sal <= 2500:
        ir = 0.1*sal
        sal_liquido = sal - (inss+sind+ir)
        print 'salario liquido eh %.2f' %(sal_liquido)
        print 'o valor do fgts eh %.2f' %(fgts)
    elif sal > 2500:
        ir = 0.2*sal
        sal_liquido = sal - (inss+sind+ir)
        print 'salario liquido eh %.2f' %(sal_liquido)
        print 'o valor do fgts eh %.2f' %(fgts)
    
if __name__ == '__main__':
    main()