# Importante

Esta es la versión “portable” por así decirlo , no hace falta tener instalado Python en el equipo

Vamos a arrancar con lo primero que me vas a decir, **¿Porque la versión “.exe” pesa 8 MB (al día de hoy) cuando la versión “.py” pesa unos pocos KB ?**. Tene en cuenta que estas ejecutando el script sin tener otras dependencias (Ejemplo Python y librerías de este), siguiendo eso, cualquier librería que se use , se va a tener que sumar al peso total del “.exe”, que es el cual va a tener “todo en uno” y va a ser más fácil de ejecutar y maniobrar. Mas abajo menciono la librería que yo use para el proceso.

Por alguna razón la versión “.exe” es detectada por algunos antivirus como Trojan/Malicious **(Falso positivo)**, yo calculo que se debe a que es un archivo único (y en consecuencia lo detectan como extraño), yo lo convertí a partir del archivo “main.py”(el que se encuentra en la carpeta que dice “base-(no necesario)”, <strong>que lo único que cambia de la versión original es que tiene una función más</strong>, que se usa para poder ubicar bien el icono durante la conversión a “.exe”, pero fuera de eso es idéntica) usando la librería “**Auto PY to EXE**” (la cual es la versión con interfaz grafica de “**PyInstaller**”)

Para crear la version ".exe"
Podes usar:

<code>pip install auto-py-to-exe</code>

o

<code>pip install pyinstaller</code>

Después si tengo tiempo voy a mandar a cada antivirus la muestra para que saquen el falso positivo

---
#### El escaneo resultante de la versión “.exe” a la fecha de 16/10/2020

https://www.virustotal.com/gui/file/88f142c430865842ccee9939d6e071e46fbd9034f635e30195a627a996b6636a/detection

---
La versión “.py” paso en limpio el test , por eso digo que es un falso positivo

#### El escaneo resultante de la versión “.py” a la fecha de 16/10/2020

https://www.virustotal.com/gui/file/bd2e5dee1f4e3a172a8d2fd98edc8a5ffef983527cdfe1f14ce61e78b13992dd/detection

https://www.virustotal.com/gui/file/d957e7660add439a1239dd5de4d7440fc8dd3ffa73c759f3448c23564c548706/detection
