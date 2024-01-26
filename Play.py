from HangedMan import HangedMan

def play(): #Este método inicia la partida y te da la opción de seguir jugando al acabar una partida
    while True:
        game = HangedMan()
        game.play()

        playAgain = input("¿Quieres jugar otra partida? (s/n): ").lower()
        if playAgain != 's':
            break

if __name__ == "__main__":
    play()