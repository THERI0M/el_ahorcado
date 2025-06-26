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
    while not fin_del_juego: # Estructura Repetitiva, Bucle Principal del Juego
        ingreso_usuario = input("\n👉 Adivina una letra o la palabra completa: ").lower()

        if len(ingreso_usuario) == 1 and ingreso_usuario.isalpha(): # Estructura Lógica, Validación de la Entrada del Usuario: determina si el usuario ha introducido una sola letra alfabética como intento.
            if ingreso_usuario in letras_adivinadas: # Estructura Lógica, Gestión de Intentos de Letras: comprueba si la letra ya fue ingresada.
                print(f"¡Oops! 😅 Ya ingresaste la letra '{ingreso_usuario}'. ¡Intenta con otra! 🧐")
            elif ingreso_usuario not in comida: # Estructura Lógica, Gestión de Intentos de Letras: si la letra no está en la palabra secreta.
                print(f"¡Mmm! ❌ La letra '{ingreso_usuario}' no está en la palabra. ¡Pierdes un intento! 😟")
                intentos -= 1
                letras_adivinadas.append(ingreso_usuario)
            else: # Estructura Lógica, Gestión de Intentos de Letras: si la letra es nueva y está en la palabra.
                print(f"¡Súper! 🎉 La letra '{ingreso_usuario}' sí está en la palabra. ¡A seguir así! 👍")
                letras_adivinadas.append(ingreso_usuario)
                for i in range(len(comida)): # Estructura Repetitiva, Revelación de Letras Adivinadas
                    if comida[i] == ingreso_usuario: # Estructura Lógica, Actualización de Guiones
                        guiones[i] = ingreso_usuario
        elif len(ingreso_usuario) == len(comida) and ingreso_usuario.isalpha(): # Estructura Lógica, Validación de la Entrada del Usuario: verifica si el usuario intentó adivinar la palabra completa.
            if ingreso_usuario in palabras_adivinadas: # Estructura Lógica, Gestión de Intentos de Palabras Completas: comprueba si la palabra ya fue intentada.
                print(f"¡Hey! 🤨 Ya ingresaste la palabra '{ingreso_usuario}'. ¡Prueba otra vez! 🔄")
            elif ingreso_usuario != comida: # Estructura Lógica, Gestión de Intentos de Palabras Completas: si la palabra es incorrecta.
                print(f"¡Uy! 👎 La palabra '{ingreso_usuario}' no es correcta. ¡Otro intento menos! 🥺")
                intentos -= 1
                palabras_adivinadas.append(ingreso_usuario)
            else: # Estructura Lógica, Gestión de Intentos de Palabras Completas: si la palabra es correcta.
                print(f"\n¡WOW! 🥳 ¡Eres un experto en comida Ecuatoriana! 👨‍🍳👩‍🍳")
                print(f"¡La palabra secreta era '{comida}'! ¡Delicioso! 💯")
                fin_del_juego = True
        else: # Estructura Lógica, Manejo de Entrada Inválida
            print("¡Alto ahí! 🛑 Por favor, ingresa SOLO UNA letra o la palabra completa. ¡No hagas trampa! 😉")

        print(grafico_ahorcado(intentos)) # Estructura Lógica implícita en la función: la función 'grafico_ahorcado' elige qué gráfico mostrar según el valor de 'intentos'.
        print(" ".join(guiones))
        print(f"Letras adivinadas: {', '.join(sorted(letras_adivinadas))} 📝")
        print(f"Intentos restantes: {intentos} ❤️")

        if "_" not in guiones: # Estructura Lógica, Comprobación de Victoria
            print(f"\n¡FELICIDADES! 🏆 Completaste la palabra: '{comida}'! ¡Eres el mejor! 🌟")
            fin_del_juego = True

        if intentos == 0 and not fin_del_juego: # Estructura Lógica, Comprobación de Derrota
            print(grafico_ahorcado(intentos))
            print(f"\n¡FATALITY! 💔 No sabes nada de comida ecuatoriana. ¡La palabra era '{comida}'! 😭")
            fin_del_juego = True

    nueva_partida = input("\n¿Dale otra partida? (s/n) 🕹️: ").lower()
    if nueva_partida == 's': # Estructura Lógica, Opción de Rejugar
        jugar_ahorcado() # Estructura Repetitiva, Recursividad para Rejugar
    else:
        print("¡Gracias por jugar, Ña! 👋 ¡Vuelve pronto por más sabores! 🇪🇨")

# Inicia el juego
if __name__ == "__main__": # Estructura Lógica, Punto de entrada del programa
    jugar_ahorcado()
