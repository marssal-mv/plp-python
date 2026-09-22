#Precos fixos dos itens do cardapio

preco_entrada = 18.90
preco_prato_principal = 45.50
preco_sobremesa = 15.00
preco_bebida = 8.50

print("=" * 40)
print("   CALCULADORA DE CONTA")
print("=" * 40)
print(f"Entrada..... R${preco_entrada:.2f}")
print(f"Prato principal..... R${preco_prato_principal:.2f}")
print(f"Sobremesa..... R${preco_sobremesa:.2f}")
print(f"Bebida..... R${preco_bebida:.2f}")
print("=" * 40)

# 2, perguntar quantidade de cada item

qtd_entrada = int(input("Quantas entradas? "))
qtd_prato_principal = int(input("Quantos pratos principais? "))
qtd_sobremesa = int(input("Quantas sobremesas? "))
qtd_bebida = int(input("Quantas bebidas? "))

# 3, Calcular o subtotal de cada item e o total

subtotal_entrada = preco_entrada * qtd_entrada
subtotal_prato_principal = preco_prato_principal * qtd_prato_principal
subtotal_sobremesa = preco_sobremesa * qtd_sobremesa
subtotal_bebida = preco_bebida * qtd_bebida

total = 0.0
total += subtotal_entrada  #atribuicao composta 
total += subtotal_prato_principal
total += subtotal_sobremesa
total += subtotal_bebida

# 4, aplicar os 10% de taxa
taxa_servico = total * 0.10
total += taxa_servico

# Gorjeta opcional 
resposta_gorjeta = input("Deseja deixar uma gorjeta extra? (sim/nao): ")
quer_gorjeta = resposta_gorjeta.strip().lower() == "sim"

gorjeta_extra = 0.0
if quer_gorjeta:
    gorjeta_extra = float(input("Qual valor de gorjeta extra deseja deixar?: R$ "))
    total_+= gorjeta_extra

# desafio extra, validacao simples (total > 200)
if total > 200:
    mensagem_validacao = "Atencao, o valor da conta ultrapassou R$ 200,00!"
else:
    mensagem_validacao = "Valor da conta dentro do esperado"

# 5, perguntar quantas pessoas dividir a conta
pessoas = int(input("Em quantas pessoas a conta sera dividida? "))

# desafio: desconto se dividido por mais de 4 pessoas
desconto = 0.0
if pessoas > 4:
    desconto = total * 0.05
    total -= desconto

valor_por_pessoa = total / pessoas

# 6, exibir tudo formatado com 2 casas decimais
print("\n" + "=" * 40)
print("     RESUMO DA CONTA")
print("=" * 40)
print(f"Subtotal entrada..... R${subtotal_entrada:.2f}")
print(f"Subtotal prato principal..... R${subtotal_prato_principal:.2f}")
print(f"Subtotal sobremesa..... R${subtotal_sobremesa:.2f}")
print(f"Subtotal bebida..... R${subtotal_bebida:.2f}")
if quer_gorjeta:
    print(f"Gorjeta extra..... R${gorjeta_extra:.2f}")
if pessoas > 4:
    print(f"Desconto (5%, +4 pessoas) ... R$ - {desconto:.2f}")
print("=" * 40)
print(f"TOTAL FINAL..... R${total:.2f}")
print(f"Valor por pessoa ({pessoas} pessoas) ... R${valor_por_pessoa:.2f}")
print("=" * 40)
print(mensagem_validacao)
print("=" * 40)
                          


