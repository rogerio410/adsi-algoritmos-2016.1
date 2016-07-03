# -*- coding: utf-8 -*-
print "QUESTÃO N°07"

A,B,C,D = input("A: "),input("B: "),input("C: "),input("D: ")
if B>C:
    if D>A:
        if C+D>A+B:
            if C > 0 and D > 0:
                if A%2 == 0:
                    print "Valores aceitos"
else:
    print "Valores nao aceitos"