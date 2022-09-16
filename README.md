# Organizador-de-keys
**Creado con el propósito de facilitar activar licencias con [ASF (ArchiSteamFarm)](https://github.com/JustArchiNET/ArchiSteamFarm).**

---
<p align="center"><img src="https://imgur.com/2XLleh9.png"></p>

Puede detectar solamente keys que estén separadas con algún tipo de espacio y también puede eliminar aquellas que parezcan incorrectas.

<strong>Ejemplo:</strong>

<p align="center"><img src="https://imgur.com/WzPHWWS.png"></p>

Nótese que hay un total de 5 keys , una se repite y ya lo maneja la aplicacion de forma automática, no hace falta tildar el casillero. Como se menciona arriba, keys que estén a medias con el texto no las puede detectar, pero si se le podría hacer una modificación a la aplicacion para que las detecte

El botón opcional que aparece ahí para tildar funciona para eliminar claves (del resultado) que cumplan alguno de los siguientes 2 parámetros

#### Keys que tengan una letra que se repita 5 veces o mas (sin ningún orden en específico)

<strong>Ejemplo:</strong>

<pre><code>AOOAO-OOAAO-OAOAO</code></pre>

En este caso la letra “A” se repite mas de 5 veces y teniendo el filtro activado se eliminaría del resultado

#### Keys que tengan una letra que se repita 4 veces o más de manera consecutiva

<strong>Ejemplo:</strong>

<pre><code>AAAAO-OOOO-OOOO</code></pre>

“A” estaría representando una letra en particular

La aplicacion también cuenta con la capacidad de abrir archivos (en formato ".txt") y también puede guardarlos

---
### Requisitos:
Para la versión “.py” solamente hace falta tener instalado [Python](https://www.python.org/)

---
### Bugs y demás:

* Intentar achicar el tamaño de la ventana demasiado
* Ingresar caracteres inválidos en los casilleros de texto

---
### Creditos:
* A [u/Jackojc](https://www.reddit.com/user/Jackojc/) por hacer la mayoría del trabajo con las funciones
