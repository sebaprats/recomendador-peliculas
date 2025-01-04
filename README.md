PROYECTO INDIVIDUAL 1 – SISTEMA DE RECOMENDACIÓN DE PELÍCULAS

OBJETIVO
 
Ingresada una película argentina por parte del usuario, crear un sistema de recomendación de otras películas nacionales. La recomendación puede ser en base a actores/actrices, género de la película, calificación, temas, etc. Definir un sistema de que agrupe dos o tres variables o bien un sistema que repregunte al usuario: quiere una película tan buena, quiere una peli de mismos actores, de mismo género, de misma temática, año, etc.

EXPLORACIÓN Y LIMPIEZA DE DATOS
Paso 1:
Lo primero que hice fue extraer una fila de cada set y copiarla en un Word para entender bien qué era cada columna, detectar cuáles estaban anidadas, chequear si estaban vinculados los ids de los dos datasets, etc. El objetivo de este trabajo fue decidir con qué data me iba a quedar para conformar mi dataset de trabajo. 

Paso 2
Del dataset Credits solo me quería quedar con la columna id y desanidar cast para quedarme solo con los nombres de los actores. Pero todos los códigos demoraban mucho la iteración. Así que decidí primero ir a Movies y quedarme solo con las pelis en español como lenguaje original. La idea es luego desanidar Credits pero antes habiéndome quedado con las pelis que me interesan.
Realicé gran parte de la limpieza de Movies y guardé lo que me quedó en un nuevo dataset (movies_dataset_limpio) para luego trabajar con ese y no correr siempre el código de limpieza.

Paso 3
A pesar de que gran parte de la limpieza fue hecha, aun quiero desanidar las columnas genre y production countries. Me parece importante conservar el género de la peli y el país para el sistema de recomendación. 
Noté que hay películas que tienen hasta 7 géneros y 8 países. A fin de simplificar, voy a quedarme con el primer género y el primer país que aparecen, aún reconociendo que como aparecen por orden alfabético puede que el primer género no sea el más importante. Y lo mismo con país.

Entiendo que esto puede generar que la recomendación no sea tan “certera” si nos basamos en género o país como fundamento de la misma. 

Paso 4
Ahora voy a reducir el dataset Credits para quedarme solo con aquellas películas de habla hispana, como paso previo a desanidar lo que necesite y luego conacatenar ambos datasets. 
Luego de filtrar y reducir el dataset Credits, voy a limpiarlo quedándome solo con el id de la película, el actor o actriz principal y el director/a.
No logré extraer todos los nombres del primer actor y del director. Funcionó con algunas filas y con otras no, y no entiendo bien por qué. Pero decidí seguir adelante y luego tal vez no le de tanta importancia a estos datos. 

FUNCIONES
Al armar la primera función, que pedía ingresar un mes de estreno, advertí que no tenia la columna con el mes. Por lo tanto, tuve que volver atrás a extraer ese dato. Algo pasó que al correr todo el código de nuevo, el dataset Credits tiraba error al levantarlo. Todo ese problema me llevó mucho tiempo, por eso cuando vi que la segunda función era indicar día de estreno decidí ignorarla para no pasar por ese problema de nuevo. 
Al armar la función de ingresar película y recibir el valor promedio de las votaciones, nos pedían que consideráramos aquellas películas con al menos 2000 votaciones. Yo bajé a 400 ese número porque mi dataset de films de habla hispana tenía 992 pelis en total.


PROBLEMAS Y MEJORAS
1-	Al desanidar las columnas crew y cast, no logré obtener todos los resultados del actor principal y del director en una nueva columna. En algunas filas reconocía al primer actor, en otras al director y en otras a ninguno.
2-	En la función de búsqueda por título, no avancé en algún método para que reconozca el título por aproximación o sugiera posibilidades. En la práctica es difícil escribir correctamente el título. Además, algunos estaban en inglés.


EDA (EXPLORATORY DATA ANALISIS)

En lo que se refiere al análisis exploratorio, lo que hice en primer lugar es ver cómo se comportaban los datos en las variables cuantitativas, como vote_average y popularidad. Identifiqué algunos outliers o anomalías más bien (una película con 10 de calificación a partir de un solo voto no puede compararse con el resto) en vote_average que podían ser filtrados fácilmente incrementando la cantidad de reseñas.
Luego armé una nube de palabras, pero no pude graficarla y que se vea bien. De todas maneras, me pregunto cuánto ayudará en el sistema de recomendación. Tal vez habría que eliminar artículos/pronombres y agruparlas en tópicos, pero no exploré esa posibilidad.


RECOMENDADOR

Para el sistema de recomendación utilicé la similitud del coseno, para la cual elegí variables como overview, genre, country y vote_average. Director y Actor hubiese querido usarlas pero tuve ese problema para desanidar cada fila. 
