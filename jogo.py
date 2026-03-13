import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']
    
    print("--- Bem-vindo ao Pedra, Papel e Tesoura! ---")
    
    while True:
        # Entrada do usuário
        usuario = input("\nEscolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
        
        if usuario == 'sair':
            print("Obrigado por jogar! Até a próxima.")
            break
            
        if usuario not in opcoes:
            print("Escolha inválida. Tente novamente!")
            continue

        # Escolha do computador
        computador = random.choice(opcoes)
        print(f"O computador escolheu: {computador}")

        # Lógica de vitória
        if usuario == computador:
            print("Empate!")
        elif (usuario == 'pedra' and computador == 'tesoura') or \
             (usuario == 'papel' and computador == 'pedra') or \
             (usuario == 'tesoura' and computador == 'papel'):
            print("Você venceu! 🎉")
        else:
            print("Você perdeu! 🤖")

if __name__ == "__main__":
    jogar()