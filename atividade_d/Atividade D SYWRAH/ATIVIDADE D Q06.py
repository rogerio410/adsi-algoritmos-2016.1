# -*- coding: utf-8 -*-
"""Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais."""
nome = raw_input('Digite o nome do vendedor: ')
salario_fixo = input('Digite o salario fixo do vendedor: ')
vendas = input('Digite o valor total vendido por esse vendedor: ')
salario_final = salario_fixo + (vendas*0.15)
print 'O vendedor %s receberá ao final deste mês a quantia de R$ %.2f' %(nome, salario_final)


