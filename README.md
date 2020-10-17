# Organizador-de-keys
**Creado con el propósito de facilitar activar licencias con [ASF (ArchiSteamFarm)](https://github.com/JustArchiNET/ArchiSteamFarm).**

---
Básicamente es una “herramienta” para acelerar un poco el proceso de registrar las keys

<p align="center"><img src="https://imgur.com/2XLleh9.png"></p>

Puede detectar solamente keys que estén separadas con algún tipo de espacio y también puede eliminar aquellas que parezcan incorrectas si así usted lo desea

<strong>Ejemplo:</strong>

<p align="center"><img src="https://imgur.com/WzPHWWS.png"></p>

Nótese que hay un total de 5 keys , una se repite y ya lo maneja el programa de forma automática, no hace falta tildar el casillero. Como se menciona arriba, keys que estén a medias con el texto no las puede detectar, pero si se le podría hacer una modificación al programa para que las detecte, tal vez en algún momento la hago

El botón opcional que aparece ahí para tildar funciona para eliminar claves (del resultado) que cumplan alguno de los siguientes 2 parámetros

#### Keys que tengan una letra que se repita 5 veces o mas (sin ningún orden en específico)

<strong>Ejemplo:</strong>

<pre><code>AOOAO-OOAAO-OAOAO</code></pre>

En este caso la letra “A” se repite mas de 5 veces y teniendo el filtro activado se eliminaría del resultado

#### Keys que tengan una letra que se repita 4 veces o más de manera consecutiva

<strong>Ejemplo:</strong>


<pre><code>AAAAO-OOOO-OOOO</code></pre>

“A” estaría representando una letra en particular

El “programa” también cuenta con la capacidad de abrir archivos (probado con archivos de texto nada más, osea “.txt”, no se que otros resultados puedan tener con otros tipos) y también puede guardarlos

---
### Requisitos:
Para la versión “.py” solamente hace falta tener instalado [Python](https://www.python.org/) y para la versión “.exe” no hace falta nada

---
### Bugs y demás:

Ya se que esta escrito como el cul* xD, en algún momento lo voy a arreglar, va, si me acuerdo ajajaj, na pero enserio, algunos errores que encontré fueron:

* Intentar achicar el tamaño de la ventana demasiado (se tendría que autoajustar, pero no lo hace, mas adelante capas lo fixeo)
* Intentar ingresar caracteres inválidos en los casilleros de texto
* Este igual creo que ya lo corregí pero hay veces que me parece que no guarda los archivos
* Y capas alguna falta de ortografía (es probable)
