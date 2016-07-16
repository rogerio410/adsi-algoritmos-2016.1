# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 18:02:44 2016

@author: wildrimak
"""

def main():
    
    salarios_atuais = 0
    salarios_reajustados = 0

    while True:
        salario = input("Informe seu salario atual: ") 
        
        if salario == 0:
            break
        elif salario < 3000:
            salarios_atuais = salarios_atuais + salario
            salario = salario * 1.25
            salarios_reajustados = salarios_reajustados + salario
        elif salario >= 3000 and salario < 6000:
            salarios_atuais = salarios_atuais + salario
            salario = salario * 1.2
            salarios_reajustados = salarios_reajustados + salario
        elif salario >= 6000 and salario < 10000:
            salarios_atuais = salarios_atuais + salario
            salario = salario * 1.15
            salarios_reajustados = salarios_reajustados + salario
        elif salario >= 10000:
            salarios_atuais = salarios_atuais + salario
            salario = salario * 1.1
            salarios_reajustados = salarios_reajustados + salario
        
        print "Seu novo salario é: %g " % salario
        
    print "A somas dos salarios antigos é: %g, A soma dos salarios reajustados é: %g e a diferença entre o somatorio do salario reajustado pelo antigo é %g " %(salarios_atuais, salarios_reajustados, salarios_reajustados - salarios_atuais)

if __name__ == "__main__":
    main()