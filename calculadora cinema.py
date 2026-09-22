# Calculadora de ida ao cinema - compra online

# Precos fixos predefinidos
preco_ingresso = 30.00
preco_pipoca = 20.00
preco_refrigerante = 10.00
taxa_conveniencia = 0.05 # 5%
desconto_combo = 5.00

print("=== Calculadora de ida ao cinema ===\n")

qtd_ingressos = int(input("Quantos ingressos deseja comprar? "))
qtd_meia_entrada = int(input("Qunatos destes ingressos sao meia entrada? "))
qtd_pipocas = int(input("Quantas pipocas deseja comprar? "))
qtd_refrigerantes = int(input("Quantos refrigerantes deseja comprar? "))

subtotal_ingressos = preco_ingresso * qtd_ingressos
desconto_meia_entrada = (preco_ingresso / 2) * qtd_meia_entrada
subtotal_ingressos -= desconto_meia_entrada

subtotal_pipocas = preco_pipoca * qtd_pipocas
subtotal_refrigerantes = preco_refrigerante * qtd_refrigerantes

#total preliminar(antes de taxa e desconto extras)
total_preliminar = subtotal_ingressos + subtotal_pipocas + subtotal_refrigerantes

#desafio extra: promocao de combo(pipoca e refrigerante -> desconto fixo)
tem_combo = qtd_pipocas >= 1 and qtd_refrigerantes >= 1
if tem_combo:
    total_preliminar -= desconto_combo 

#aplica a taxa de conveniencia de 5% sobre o valor total
total_final = total_preliminar + (total_preliminar * taxa_conveniencia)

#pergunta entre quantas pessoas o valor sera dividido
qtd_pessoas = int(input("Entre quantas pessoas o valor sera dividido? "))
valor_por_pessoas = total_final / qtd_pessoas

#desafio extra: alerta de orcamento
passeio_caro = valor_por_pessoas > 40.00

#exibe o recibo formatado
print("\n==== Recibo ====")
print(f"ingressos ({qtd_ingressos}x, sendo {qtd_meia_entrada} meia): R${subtotal_ingressos:>8.2f}")
print(f"Pipocas ({qtd_pipocas}x): R${subtotal_pipocas:8.2f}")
print(f"Refrigerantes ({qtd_refrigerantes}x): R${subtotal_refrigerantes:8.2f}")

if tem_combo:
    print(f"desconto combo (pipoca + refrigerante): R$ -R${desconto_combo:.2f}")

print(f"Taxa de conveniencia (5%): R$ {(total_preliminar * taxa_conveniencia):>8.2f}")
print("-----------------------------")
print(f"Total final: R$ {total_final:.2f}")
print(f"Dividido entre {qtd_pessoas} pessoa(s): R$ {valor_por_pessoa:.2f} por pessoa")
print("=============================")
print(f"Passeio saiu caro? {passeio_caro}")