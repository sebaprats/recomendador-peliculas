# SISTEMA DE RECOMENDACIÓN DE PELÍCULAS (PROYECTO HENRY)

1️⃣ OBJETIVO
 
Ingresada una película de habla hispana por parte del usuario, creé un sistema de recomendación de otras películas cuyo idioma original también es el español.

https://recomendador-de-peliculas-fast-api-y.onrender.com/docs
2- EXPLORACIÓN Y LIMPIEZA DE DATOS

Paso 1:
Lo primero que hice fue extraer una fila de cada set y copiarla en un Word para entender bien qué era cada columna, detectar cuáles estaban anidadas, chequear si estaban vinculados los ids de los dos datasets, etc. El objetivo de este trabajo fue decidir con qué data me iba a quedar para conformar mi dataset de trabajo. 

Paso 2
Del dataset Credits solo me quería quedar con la columna id y desanidar cast para quedarme solo con los nombres de los actores. Pero todos los códigos que implementaba demoraban mucho la iteración. Así que decidí primero ir a Movies y quedarme solo con las pelis en español como lenguaje original. La idea es desanidar Credits pero antes habiéndome quedado con las pelis que me interesan.

Realicé gran parte de la limpieza de Movies y guardé lo que me quedó en un nuevo dataset (movies_dataset_limpio) para luego trabajar con ese y no correr siempre el código de limpieza.

Paso 3
A pesar de que gran parte de la limpieza fue hecha, aun quiero desanidar las columnas genre y production countries. Me parece importante conservar el género de la peli y el país para el sistema de recomendación. Noté que hay películas que tienen hasta 7 géneros y 8 países. A fin de simplificar, voy a quedarme con el primer género y el primer país que aparece, aún reconociendo que como aparecen por orden alfabético puede que el género o el país no sean los más importantes y haya cierto sesgo. Entiendo que esto puede generar que la recomendación no sea tan “certera” si nos basamos en género o país como fundamento de la misma. 

Paso 4
Luego reduje el dataset Credits para quedarme solo con aquellas películas de habla hispana, como paso previo a desanidar lo que necesite y luego conacatenar ambos datasets. 
Luego de filtrar y reducir el dataset Credits, quise limpiarlo para quedarme solo con el id de la película, el actor o actriz principal y el director/a, pero no logré extraerlos en todas las filas. El código funcionó con algunas y con otras no, y no entiendo bien por qué. Pero decidí seguir adelante.

3- FUNCIONES
Al armar la primera función, que pedía ingresar un mes de estreno, advertí que no tenia la columna con el mes. Por lo tanto, tuve que volver atrás a extraer ese dato. Algo pasó que al correr todo el código de nuevo, el dataset Credits tiraba error al levantarlo. Todo ese problema me llevó mucho tiempo, por eso cuando vi que la segunda función era indicar día de estreno decidí ignorarla para no pasar por ese problema de nuevo. 

Al armar la función de ingresar película y recibir el valor promedio de las votaciones, nos pedían que consideráramos aquellas películas con al menos 2000 votaciones. Yo bajé a 400 ese número porque mi dataset de films de habla hispana tenía 992 pelis en total.



4- EDA (EXPLORATORY DATA ANALISIS)

En lo que se refiere al análisis exploratorio, creo que en este caso, al ser la mayoría variables cualitativas, no aportó mucho al trabajo. De todas maneras, intenté hacer algún cruce de datos a ver qué me arrojaba. 

Lo que hice en primer lugar es ver cómo se comportaban los datos en las variables cuantitativas, como vote_average y popularidad. Identifiqué algunos outliers, o anomalías más bien, (una película con 10 de calificación a partir de un solo voto no puede compararse con el resto) en vote_average que podían ser filtrados fácilmente incrementando la cantidad de reseñas (vote_count) a considerar.

Luego armé una nube de palabras, pero no pude graficarla y que se vea bien. De todas maneras, me pregunto cuánto ayudará en el sistema de recomendación. Tal vez habría que eliminar artículos/pronombres (entiendo que luego la función stop_words hace justamente eso) y agruparlas en tópicos, pero no exploré esa posibilidad.


5- RECOMENDADOR

En cuanto al recomendador, las mayores complicaciones las tuve con hacer correr bien Fast Api primero y con la creación del repo y el commit en Git Hub. Me llevó bastantes horas identificar los problemas, de hecho eliminé y cree de nuevo el repo dos o tres veces hasta entender cómo funcionaba bien.

Luego, utilicé la similitud del coseno, para la cual elegí variables como overview, genre, country y vote_average. Director y Actor hubiese querido usarlas pero tuve ese problema para desanidar cada fila.

6- PROBLEMAS Y MEJORAS

a-	Al desanidar las columnas crew y cast, no logré obtener todos los resultados del actor principal y del director en una nueva columna. En algunas filas reconocía al primer actor, en otras al director y en otras a ninguno. No entendí por qué, estuve varias horas tratando de resolverlo pero no pude y decidí seguir adelante.

b-	En la función de búsqueda por título, no avancé en algún método para que reconozca el título por aproximación o sugiera posibilidades. En la práctica es difícil escribir correctamente el título. Además, algunos están en inglés y el usuario no tiene por qué saberlo.

c- Tuve una duda con la función StopWords, porque uno le indica un idioma especifico. Pero qué pasa cuando, en este caso, tenemos títulos y reseñas en español o inglés. 

d- Por último, no sé si entiendo bien cómo trabaja la similitud del coseno, qué es lo que pondera y cómo lo hace para recomendar lo que recomienda y eventualmente hacer algún ajuste si no es el resultado buscado.
