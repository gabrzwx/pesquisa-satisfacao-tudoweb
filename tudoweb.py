# Inicialização dos contadores
cont_excelente = 0
cont_ruim = 0

print("--- Pesquisa de Satisfação TudoWeb ---")

for i in range(1, 51):
    print(f"\nEntrevistado nº {i}")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print("Opiniões: 1 - EXCELENTE | 2 - BOM | 3 - RUIM")
    opn = int(input("Sua resposta: "))

    match opn:
        case 1:
            cont_excelente += 1
        case 3:
            cont_ruim += 1
        case 2:
            pass 
        case _:
            print("Opção inválida! Este voto não será contabilizado.")

print("\n" + "="*30)
print("      RESULTADO DA PESQUISA")
print("="*30)
print(f"Quantidade de respostas EXCELENTE: {cont_excelente}")
print(f"Quantidade de respostas RUIM:      {cont_ruim}")
print("="*30)