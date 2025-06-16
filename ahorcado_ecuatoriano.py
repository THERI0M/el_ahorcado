import random
palalabras=("encebollado", "ceviche", "hornado", "fritada", "corviche", "tonga", "llapingacho", "fanesca", "morada", "locro", "bolon", "tigrillo", "cuy", "chugchucaras", "encocado", "maito", "yahuarlocro", "chonta", "mote", "hallullas", "quimbolito", "humitas" )
palabra_secreta=random.choice(palalabras)
palabra_mostrada=""
for guiones in palabra_secreta:
    palabra_mostrada += "_"
grafico6 = ('''
           +---+
           |   |
               |
               |
               |
               |
        ========''')
grafico5 = ('''
           +---+
           |   |
          🙄​   |
               |
               |
               |
        ========''')
grafico4 = ('''
           +---+
           |   |
          😳   |
           |   |
               |
               |
        ========''')
grafico3 = ('''
           +---+
           |   |
          ​😨​   |
          /|   |
               |
               |
        ========''')
grafico2 = ('''
           +---+
           |   |
          ​🤢​   |
          /|\  |
               |
               |
        ========''')
grafico1 = ('''
           +---+
           |   |
          ​​🤪​   |
          /|\  |
          /    |
               |
        ========''')
grafico0 = ('''
           +---+
           |   |
          ​​​😑​​   |
          /|\  |
          / \  |
               |
        ========''')

letras_intentadas=""
intentos_restantes=6
print("<<<BIENVENIDO AL AHORCADO>>>")
print("\nde la comida ecuatoriana 🍤")

# Bucle principal
while True:
    # Mostrar el gráfico
    if intentos_restantes==6:
        print(grafico6)
    elif intentos_restantes==5:
        print(grafico5)
    elif intentos_restantes==4:
        print(grafico4)
    elif intentos_restantes==3:
        print(grafico3)
    elif intentos_restantes==2:
        print(grafico2)
    elif intentos_restantes==1:
        print(grafico1)
    elif intentos_restantes==0:
        print(grafico0)

    print(f"Palabra: {palabra_mostrada} 🤓")
    print(f"Letras INGRESADAS: {letras_intentadas} ✏️")
    print(f"Te quedan {intentos_restantes} intentos 😉")

    letra_ingresada_por_usuario = input("\nIngresa una letra: ").lower()

    # Después de pedir la letra se contabiliza y se revisa; si ya ha sido ingresada.

    
    contador_de_letras = 0
    for char_val in letra_ingresada_por_usuario:
        contador_de_letras += 1
    if contador_de_letras != 1:
        print("¡Por favor, ingresa SOLO UNA letra!")
        continue
    if letra_ingresada_por_usuario in letras_intentadas:
        print(f"¡Ya probaste la letra '{letra_ingresada_por_usuario}'! No lo olvides 😱")
        continue
    letras_intentadas += letra_ingresada_por_usuario + " "

    # Proceso cuando la letra si se encuentra en la palabra.

    if letra_ingresada_por_usuario in palabra_secreta:
        print(f"La letra '{letra_ingresada_por_usuario}' está en la palabra 👍")
        nueva_palabra_mostrada = ""

        # Ubicar las letras ingresadas en palabras temporales
        palabra_temporal = ""
        for letra_secreta in palabra_secreta:
            palabra_temporal += letra_secreta
        palabra_temporal_mostrada = ""
        for letra_mostrada in palabra_mostrada:
            palabra_temporal_mostrada += letra_mostrada
        # Comparamos letra por letra para ubicarlas        
        posicion_actual_en_palabra = 0
        union_de_letras = ""               
        for letra_secreta in palabra_temporal:            
            posicion_palabra_mostrada = 0
            posicion_de_letra = '_'      
            for letra_mostrada in palabra_temporal_mostrada:
                if posicion_palabra_mostrada == posicion_actual_en_palabra:
                    posicion_de_letra = letra_mostrada
                    break # Encontramos el carácter en la posición correcta
                posicion_palabra_mostrada += 1
            if letra_secreta == letra_ingresada_por_usuario:
                union_de_letras += letra_ingresada_por_usuario
            elif posicion_de_letra != '_':
                union_de_letras += posicion_de_letra
            else:
                union_de_letras += '_'            
            posicion_actual_en_palabra += 1 # Avanzamos en la posición
        palabra_mostrada = union_de_letras # Actualizamos la palabra que el usuario ve
    else:
        print(f"¡Incorrecto! La letra '{letra_ingresada_por_usuario}' NO está en la palabra.")
        intentos_restantes -= 1

    # Reglas para que el juego termine
    # Se verifica si se ganó (si no hay guiones en palabra_mostrada)
    juego_ganado = True
    for char_displayed in palabra_mostrada:
        if char_displayed == '_':
            juego_ganado = False
            break

    if juego_ganado:
        print(f"\nCompletaste la palabra: {palabra_mostrada}")
        print(f"\nWOW eres un experto en comida Ecuatoriana \nLa palabra secreta era {palabra_secreta}!")
        break

    # Se Verifica si perdió (no quedan intentos)
    if intentos_restantes == 0:
        print(f"\nPalabra actual: {palabra_mostrada}")
        print(f"\nNo sabes nada de comida ecuatoriana, La palabra era {palabra_secreta}. ​😡​")
        print(grafico0)
        break

print("\nNos Vemos Ña!")
