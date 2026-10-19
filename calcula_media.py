# -*- coding: utf-8 -*-
"""
Cálculo da média aritmética simples de 3 notas informadas pelo usuário.
"""

print("* * * CÁLCULO DA MÉDIA * * *\n")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nO valor da média final é: {media:.2f}")
input("\nPressione Enter para sair...")
