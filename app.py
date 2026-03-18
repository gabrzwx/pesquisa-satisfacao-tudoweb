aparelho = input("Digite o nome do aparelho: ")
potenc = float(input("Digite a potência em watts(W): "))
tempomedio = float(input("Digite o tempo médio de uso diário em horas: "))

tempo_mensal = (potenc * tempomedio * 30) / 1000

valor_kWh = 0.70
valor_total = tempo_mensal * valor_kWh

print(f"Aparelho selecionado: {aparelho}")
print(f"Consumo estimado: {tempo_mensal:.2f} kWh/mês")
print(f"Valor total estimado: R$ {valor_total:.2f}")