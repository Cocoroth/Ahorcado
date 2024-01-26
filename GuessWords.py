import random

class GuessWords: #Las palabras disponibles a adivinar
    @staticmethod
    def wordSelector():
        guessWords = ["koala", "calvo", "precipicio", "experimento", "balanza",
                      "tiroteo", "negocios", "borde", "apellido", "marea",
                      "peruano", "turista", "perforar", "hoja", "aplauso",
                      "torcer", "especialista", "canica", "bostezo", "guirnalda",
                      "especular", "carnicero", "canguro", "sabana", "casco",
                      "picante", "arroz", "harina", "mapa", "billetes",
                      "invitacion", "colmena", "anciano", "caminata", "amontonar",
                      "consulta", "suegra", "elegido", "abanico", "pizarra"]
        return random.choice(guessWords)