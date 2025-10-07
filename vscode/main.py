# Exibe uma mensagem de boas-vindas com nome e sobrenome 

print('Bem-vindo ao sistema do JJ!') 

 

# Solicita ao usuário o valor base do plano e a idade do cliente 

valorBase = float(input('Digite o valor base do plano (R$): ')) 

idade = int(input('Digite a idade do cliente: ')) 

 

# Define a porcentagem de acordo com a faixa etária 

# Utiliza estruturas if, elif e else conforme exigido 

if idade >= 0 and idade < 19: 

    porcentagem = 100  # 100% do valor base 

elif idade >= 19 and idade < 29: 

    porcentagem = 150  # 150% do valor base 

elif idade >= 29 and idade < 39: 

    porcentagem = 225  # 225% do valor base 

elif idade >= 39 and idade < 49: 

    porcentagem = 240  # 240% do valor base 

elif idade >= 49 and idade < 59: 

    porcentagem = 350  # 350% do valor base 

else: 

    porcentagem = 600  # 600% do valor base 

 

# Calcula o valor mensal do plano com base na porcentagem 

valorMensal = valorBase * (porcentagem / 100) 

 

# Exibe o valor mensal do plano formatado com duas casas decimais 

print(f'O valor mensal do plano é: R$ {valorMensal:.2f}') 