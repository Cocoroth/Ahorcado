from HangedMan import HangedMan

def play():
    while True:
        game = HangedMan()
        game.play()

        playAgain = input("¿Quieres jugar otra partida? (s/n): ").lower()
        if playAgain != 's':
            break

if __name__ == "__main__":
    play()