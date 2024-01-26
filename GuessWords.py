import random

class GuessWords:
    @staticmethod
    def wordSelector():
        guessWords = ["koala", "calvo", "precipicio", "experimento", "balanza"
                      "tiroteo", "negocios", "borde", "apellido", "marea"
                      "peruano", "turista", "perforar", "hoja", "aplauso"
                      "torcer", "especialista", "canica", "bostezo", "guirnalda"]
        return random.choice(guessWords)