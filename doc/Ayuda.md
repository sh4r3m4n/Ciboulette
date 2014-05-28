# Ciboulette

Es una red social 100% libre, entre pares, descentralizada y distribuida

Con un simple blog y lectores de Noticias (RSS, Atom, RDF) se crea una red social libre en la que cada persona publica novedades directamente desde su computadora.
Y es accesible desde cualquier computadora con Tor gracias a sus servicios ocultos.

## Comandos de la terminal

Este es un método muy simple para usar **Ciboulette** podes acceder a tu terminal desde el menú de inicio, por lo general esta en la sección accesorio.

<pre>cat ~/.ciboulette/hostname</pre>

Es el dirección de tu nodo (pasala a tus amig@s)

<pre>ciboulette -n http://3orzmu3bziaoivpg.onion</pre>

Es para agregar a un nodo a tu lector de [novedades](/articles/novedades/)

<pre>ciboulette -b http://3orzmu3bziaoivpg.onion</pre>

Es para quitar un nodo a tu lector de [novedades](/articles/novedades/)

<pre>echo "Este es el contenido"  | ciboulette -a "Artículo en la terminal"</pre>

Publicar un articulo

<pre>ciboulette -l</pre>

## Ciboulette en internet

Si alguno de tus amig@s no tiene ciboulette podes pasarle la dirección para acceder desde internet.

Podes usar [tor2web](https://es.wikipedia.org/wiki/.onion#tor2web) para esto existe varios servidores públicos de este servicio.

* [tor2web.org](https://tor2web.org)
* [onion.to](https://onion.to)

## Ciboulette en [Cyanogem](http://www.cyanogenmod.org/) o Andriod

Para pasar tu dirección a un celular o tablet podes usar el [QR](/qr.png) y reconocerla con [Barcode Scanner](https://f-droid.org/repository/browse/?fdfilter=qr&fdid=com.google.zxing.client.android).

Mientras este prendido y conectado tu nodo de Ciboulette, podes conectarte con tu celular usando [GibberBot](https://f-droid.org/repository/browse/?fdfilter=orbot&fdid=info.guardianproject.otr.app.im) con [Orbot](https://f-droid.org/repository/browse/?fdfilter=orbot&fdid=org.torproject.android). 

Para leer las novedades se puede usar [Feedex](https://f-droid.org/repository/browse/?fdfilter=feedex&fdid=net.fred.feedex) tenes que configurar el proxy en `127.0.0.1` puerto `8118`. Con agregar tu dirección de [RSS de novedades](/novedades.xml) basta :D

_Todas estas aplicaciones estan disponibles en [F-droid](http://f-droid.org/)_

## Filosofía UNIX

Ciboulette sigue los principios de la **filosofía Unix** en su construcción, el modo en que se comunican sus nodos y en la integración con el sistema operativo, o sea una red social con filosofía Unix

* **Regla de Modularidad:** Escribe partes simples, conectadas por interfaces simples.
* **Regla de Claridad:** ser Claro es mejor que ser ingenioso.
* **Regla de Composición:** Diseña programas para que se conecten a otros programas.
* **Regla de Separación:** Separa las Reglas del funcionamiento; separa los interfaces de los mecanismos.
* **Regla de Simplicidad:** Diseña para la simplicidad; añade complejidad sólo donde sea estrictamente necesario.
* **Regla de Parsimonia:** Escribe un programa complejo sólo cuando sea evidente que no existe otra solución posible.
* **Regla de Transparencia:** Diseña para la visibilidad, para hacer más fácil la inspección y la corrección de fallos.
* **Regla de Robustez:** la Robustez es hija de la transparencia y la simplicidad.
* **Regla de Representación:** Convierte el conocimiento en datos, para que la lógica de los programas pueda ser estúpida y robusta.
* **Regla de Mínima Sorpresa:** En diseño de interfaces, haz siempre lo menos sorprendente.
* **Regla de Silencio:** Cuando un programa no tenga nada sorprendente que decir, no debería decir nada.
* **Regla de Reparación:** Cuando tengas que mostrar un error, falla estridentemente y lo antes posible.
* **Regla de Economía:** el tiempo del programador es caro; consérvalo sobre el tiempo de la máquina.
* **Regla de Generación:** Evita hacer cosas a mano; escribe programas que escriban programas siempre que puedas.
* **Regla de Optimización:** Prototipa antes de pulir. Haz que funcione antes de optimizarlo.
* **Regla de Diversidad:** Desconfía de todo lo que diga _"esta es la única forma correcta"_.
* **Regla de Extensibilidad:** Diseña para el futuro, porque estará aquí antes de lo que piensas.
