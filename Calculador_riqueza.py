# Coletando os dados
nome = input("Digite seu nome: ")
salario_meta = float(input("Qual salário você quer ganhar como Dev Senior? R$ "))
estagio_valor = float(input("Quanto você espera ganhar no primeiro estágio? R$ "))

# Cálculo de evolução (exemplo: dobrar o salário a cada ano)
anos_para_meta = 0
salario_atual = estagio_valor

while salario_atual < salario_meta:
    salario_atual *= 2  # Simulando um salto de carreira/promoção
    anos_para_meta += 1

# Resultado na tela
print("-" * 30)
print(f"Fala, {nome}!")
print(f"Para chegar em R$ {salario_meta:.2f}, saindo de R$ {estagio_valor:.2f}...")
print(f"Você precisará de aproximadamente {anos_para_meta} saltos de carreira.")
print("FOCO NO PYTHON E NO INGLÊS!")
print("-" * 30)
