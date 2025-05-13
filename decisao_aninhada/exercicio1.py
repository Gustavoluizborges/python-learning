idade_pessoa = int(input("Digite sua idade "))

if idade_pessoa < 16:
    print("Não Eleitor")
elif idade_pessoa >= 18 and idade_pessoa <= 65:
    print("Eleitor Obrigatório")
elif idade_pessoa >= 16 and idade_pessoa <= 18 or idade_pessoa > 65:
    print("Eleitor Facultativo")