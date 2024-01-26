from GuessWords import GuessWords

class HangedMan:
    def __init__(self):
        self.secretWord = GuessWords.wordSelector()
        self.remainingAttempts = 6
        self.correct = []
        self.attempted = []

    def showGameBoard(self):
        gameBoard = ""
        for letter in self.secretWord:
            if letter in self.correct:
                gameBoard += letter + " "
            else:
                gameBoard += "_ "
        return gameBoard

    def showHangedMan(self, remainingAttempts):
            HangedMan = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
            print(HangedMan[6 - remainingAttempts])

    def play(self):
        print("¡Bienvenido al ahorcado!")
        print(
            "Intenta adivinar la palabra secreta introduciendo una letra o adivina la palabra, tienes un total de 6 intentos ¡pero cuidado, si adivinas la palabra y es incorrecta perderás automáticamente!")
        print("La palabra tiene", len(self.secretWord), "letras.")

        while self.remainingAttempts > 0:
            print("\nIntentos restantes:", self.remainingAttempts)
            self.showHangedMan(self.remainingAttempts)
            gameBoard = self.showGameBoard()
            print(gameBoard)

            if "_" not in gameBoard:
                print("¡Felicidades! ¡Has adivinado la palabra!")
                return True

            letra = input("Introduce una letra o intenta adivinar la palabra: ").lower()

            if len(letra) > 1:
                if letra == self.secretWord:
                    print("¡Felicidades! ¡Has adivinado la palabra!")
                    return True
                else:
                    print("Has perdido, la palabra era:", self.secretWord)
                    return False

            if letra in self.attempted:
                print("Ya has intentado esa letra. ¡Intenta con otra!")
                continue

            self.attempted.append(letra)

            if letra in self.secretWord:
                self.correct.append(letra)
                print("¡Bien hecho! La letra está en la palabra.")
            else:
                self.remainingAttempts -= 1
                print("La letra no está en la palabra. Te quedan", self.remainingAttempts, "intentos.")

        else:
            self.showHangedMan(self.remainingAttempts)
            print("Te has quedado sin intentos, la palabra era:", self.secretWord)
            return False
