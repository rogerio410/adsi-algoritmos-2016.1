# -*- coding: utf-8 -8-
"""6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)"""
velokm = input("Insira um velocidade em k/h: ")
veloms = velokm / 3.6
print "%.1f km/h equivale a %.1f m/s" % (velokm, veloms)