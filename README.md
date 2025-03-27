# asteroids
asteroids-game self-made engine

## NOTA DEL COMMIT 3/27/25

## DID    

ya se actualiza el score. 
Solo crear dos nuevas mid rocks si se impacta una roca grande 
actualizar que las rocas se tomen de un sprite en lugar de un spritesheet
colisiones con rocas y el jugador
Respawnear el jugador cuando impacte con una roca y restarle una vida
sistema de vidas
El bucle de juego completo: luego de perder todas las vidas nos re-envia al menu principal y podemos volver a jugar

## TO DO 

3. hud para las vidas
4. nivel de game over
5. sistema de particulas para la nave y 
6. las rocas cuando se destrozen
7. volver una clase la encargada de actualizar valores para los textos de un hud

## To-do al 3/20/2025


1. Player: 

    * Crear un sistema de vidas para el jugador. (Logica para pederla esta en la zona de abajo. )

    * Physics: 
        - Si un asteroid alcanza la nave del jugador debe de registrarse una colision y restarsele una vida al jugador. 


2. Rocks

    * Representation: 

        - Crear rocas de distintos tamaños. 

    * Localization
    
    * Physics: 

        - Cuando una rock sea impactada por un proyectil debe dividirse en dos asteroides mas pequeños pero con mayor velocidad cada uno con un leve grado de inclinacion. 

3. Bullets

    Nada (Por ahora)

4. Engine

    * Hud 
        
        - Crear un sistema de HUD donde se muestren las cantidad de vidas restantes del jugador y el score alcanzado

    * Niveles 
        
        - Crear la logica para que los niveles sean piezas independientes que contengan todos los "gameobjs " y otras configuraciones, ademas de tener la posibilidad de cargar dicha configuracion y "cargar" el nivel. ASi poder crear transiciones entre niveles y etc.     

        * Nivel Inicial: 

            - Pantalla de bienvenida
            - Informacion de los controles
            - Boton para inicar nueva partida
        
        * Nivel Jugable: 

            - El ambiente donde jugara el jugador. 
            
            - Victoria: NO HAY. con cada impacto a un asteroide ganaras puntos y conforme pase el tiempo los asteroides se haran mas rapidos. 

            - Derrota: 3 vidas y cada vez que impacte un asteroide con el jugador perdera un vida. Cuando las vidas lleguen a cero se presentara un anuncio de game over y regresara a la primera pantalla.  

NOTA: 
la informacion del juego estara dividido en niveles. Cada nivel sera un archivo json, y durante la ejecucion del programa podre cambiar entre niveles simplemente pasandole otro archivo json y asio puedo ahorrar recursos porque el juego carga una vez el nivel y no se preocupa por el contenido de los otros

## Ready al 3/18/2025

1. Player: 
    
    * Representation

        - Logica para cargar sprite del obj y cambiarlo en base a si estas presionado la tecla de acelerar o no. 

    * Localization

        - Posiciones iniciales

    * physics
        - Aceleracion 
        - Frenado paulatino cuando se deja de acelerar
        - Rebotado en las esquinas de la pantalla 

2. Rocks

    * Representation
        
        - Logica para cargar sprite del obj.

    * Localization

        - localizaciones pre-establecidas
    
    * physics
        
        - Colision con las balas
        - Rebotado en las esquinas de la pantalla 
        - Movimiento basado en velocidad random. 

3. Bullets

    * Representation
        
        - Logica para cargar sprite del obj y cambiarlo en base a si estas presionado la tecla de acelerar o no. 

    * Localization

        - Segun la inclinacion del jugador y la posicion el disparo tiene una localization iniical
    
    * physics
        
        - Colision con las rocas
        - Rebotado en las esquinas de la pantalla 



