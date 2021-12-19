# JUEGO HUNDIR LA FLOTA

### Introducción:
Hemos creado nuestro propio juego de Hundir la Plota en Python. Para el desarrollo del programa hemos utilizado conocientos de la librería `numpy`, módulos, bucles, funciones y colecciones de Python.


### ¿Cómo funciona el juego?
1. Hay dos jugadores: tu y la maquina
2. Un **tablero de 10 x 10** posiciones donde irán los barcos.
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria. Los barcos son:**
    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora

4. Tanto tu, como la maquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
5. Funciona por turnos y empiezas tu.
6. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la maquina.
7. En los turnos de la maquina, si acierta, también le vuelve a tocar. ¿Dónde dispara la maquina? A un punto aleatorio en tu tablero.
8. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.
9. El juego te preguntará si quieres jugar otra partida.


#### Creadores:
Miguel A. Batalla.
Natalia Fernández García.
19/12/21