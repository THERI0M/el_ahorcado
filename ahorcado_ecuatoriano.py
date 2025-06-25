import random

def palabra_random():    
    palabras = ["encebollado", "ceviche", "hornado", "fritada", "corviche", "tonga", "llapingacho", "fanesca", "morada", "locro", "bolon", "tigrillo", "cuy", "chugchucaras", "encocado", "maito", "yahuarlocro", "chontacuro", "mote", "hallullas", "quimbolito", "humitas"]
    return random.choice(palabras)

def grafico_ahorcado(intentos):
    etapas = [   # DIBUJO AHORCADO POR ETAPAS
                 """
                    +---+
                    |   |
                    ​😑​  |
                    /|\ |
                    / \ |
                        |
                    ========
                 """,
                 """
                    +---+
                    |   |
                    ​🤪​  |
                    /|\ |
                    /   |
                        |
                    ========
                 """,
                 """
                    +---+
                    |   |
                    ​🤢​  |
                    /|\ |
                        |
                        |
                    ========
                 """,
                 """
                    +---+
                    |   |
                    ​😨​  |
                    /|  |
                        |
                        |
                    ========
                 """,
                 """
                    +---+
                    |   |
                    😳  |
                    |   |
                        |
                        |
                    ========
                 """,
                 """
                    +---+
                    |   |
                    🙄​  |
                        |
                        |
                        |
                    ========
                 """,
                 """
                    +---+
                    |   |
                        |
                        |
                        |
                        |
                    ========
                 """
    ]
    return etapas[intentos]
# DEFINO VARIABLES
def jugar_ahorcado():     
    comida = palabra_random()
    guiones = ["_"] * len(comida)
    letras_adivinadas = []
    palabras_adivinadas = []
    intentos = 6
    fin_del_juego = False
# DETERMINO LA PARTE VISUAL PARA EL USUARIO
    print("<<<🎉 BIENVENIDO AL AHORCADO 🎉>>>")
    print("\n¡De la comida ecuatoriana! 🍲😋")
    print(grafico_ahorcado(intentos))
    print(" ".join(guiones))
    print(f"La palabra tiene {len(comida)} letras. 🤔")
# BUCLE PRINCIPAL
    while not fin_del_juego:
        ingreso_usuario = input("\n👉 Adivina una letra o la palabra completa: ").lower()

        if len(ingreso_usuario) == 1 and ingreso_usuario.isalpha():
            if ingreso_usuario in letras_adivinadas:
                print(f"¡Oops! 😅 Ya ingresaste la letra '{ingreso_usuario}'. ¡Intenta con otra! 🧐")
            elif ingreso_usuario not in comida:
                print(f"¡Mmm! ❌ La letra '{ingreso_usuario}' no está en la palabra. ¡Pierdes un intento! 😟")
                intentos -= 1
                letras_adivinadas.append(ingreso_usuario)
            else:
                print(f"¡Súper! 🎉 La letra '{ingreso_usuario}' sí está en la palabra. ¡A seguir así! 👍")
                letras_adivinadas.append(ingreso_usuario)
                for i in range(len(comida)):
                    if comida[i] == ingreso_usuario:
                        guiones[i] = ingreso_usuario
        elif len(ingreso_usuario) == len(comida) and ingreso_usuario.isalpha():
            if ingreso_usuario in palabras_adivinadas:
                print(f"¡Hey! 🤨 Ya ingresaste la palabra '{ingreso_usuario}'. ¡Prueba otra vez! 🔄")
            elif ingreso_usuario != comida:
                print(f"¡Uy! 👎 La palabra '{ingreso_usuario}' no es correcta. ¡Otro intento menos! 🥺")
                intentos -= 1
                palabras_adivinadas.append(ingreso_usuario)
            else:
                print(f"\n¡WOW! 🥳 ¡Eres un experto en comida Ecuatoriana! 👨‍🍳👩‍🍳")
                print(f"¡La palabra secreta era '{comida}'! ¡Delicioso! 💯")
                fin_del_juego = True
        else:
            print("¡Alto ahí! 🛑 Por favor, ingresa SOLO UNA letra o la palabra completa. ¡No hagas trampa! 😉")

        print(grafico_ahorcado(intentos))
        print(" ".join(guiones))
        print(f"Letras adivinadas: {', '.join(sorted(letras_adivinadas))} 📝")
        print(f"Intentos restantes: {intentos} ❤️")

        if "_" not in guiones:
            print(f"\n¡FELICIDADES! 🏆 Completaste la palabra: '{comida}'! ¡Eres el mejor! 🌟")
            fin_del_juego = True

        if intentos == 0 and not fin_del_juego:
            print(grafico_ahorcado(intentos))
            print(f"\n¡FATALITY! 💔 No sabes nada de comida ecuatoriana. ¡La palabra era '{comida}'! 😭")
            fin_del_juego = True

    nueva_partida = input("\n¿Dale otra partida? (s/n) 🕹️: ").lower()
    if nueva_partida == 's':
        jugar_ahorcado()
    else:
        print("¡Gracias por jugar, Ña! 👋 ¡Vuelve pronto por más sabores! 🇪🇨")

# Inicia el juego
if __name__ == "__main__":
    jugar_ahorcado()
