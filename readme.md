# Análisis de Tendencias en YouTube

## Universidad Peruana de Ciencias Aplicadas
**Sección:** CC52  
**Grupo:** 1  
**Curso:** Fundamentos de Data Science  
**Profesor(a):** Nérida Isabel Manrique Tunque  
**Título:** Análisis de tendencias en YouTube  

**Autores:**  
- Tomás Edgar Ninán Melo (u201625763)  
- José Guillermo Melgar Puertas (u202111660)  
- Alfredo Mauricio Aragón Ovalle (u202210494)  
- Rody Sebastian Vilchez Marin  (u202216562)
**Periodo:** 2024-01

## Introducción
En el mundo digital actual, YouTube se ha consolidado como una de las plataformas más influyentes para compartir y consumir contenido multimedia. Con miles de millones de usuarios activos mensuales, YouTube no solo ofrece entretenimiento, sino también educación, noticias y una forma de conectar con comunidades globales. La diversidad de contenido en YouTube se agrupa en varias categorías, que van desde la música y los deportes hasta la ciencia y la tecnología, pasando por blogs personales y tutoriales de estilo de vida.

El análisis de datos de YouTube permite entender mejor las tendencias de consumo, las preferencias de los usuarios y las dinámicas de interacción. Este conocimiento es valioso tanto para los creadores de contenido como para los profesionales del marketing, ya que les ayuda a optimizar sus estrategias de contenido y maximizar su alcance y participación.

Este informe presenta un análisis exhaustivo de un conjunto de datos de videos de YouTube del mes de enero de 2021. Utilizando la metodología CRISP-DM (Cross Industry Standard Process for Data Mining), se busca explorar y entender cómo diferentes categorías de videos se desempeñan en términos de vistas, likes y comentarios.

## Metodología CRISP-DM

### 1. Comprensión del Negocio
En el ecosistema actual de medios digitales, YouTube se destaca no solo como una plataforma de entretenimiento, sino también como un motor económico significativo que impulsa la creación de contenido y las estrategias de marketing digital. La capacidad de entender qué tipos de contenido resuenan más con las audiencias puede marcar la diferencia entre el éxito y el fracaso de una estrategia de contenido.

#### Objetivos del Análisis
El principal objetivo de este análisis es comprender las dinámicas y tendencias de visualización, interacción y popularidad de diferentes categorías de videos en YouTube. Específicamente, buscamos responder las siguientes preguntas:
1. ¿Qué categorías de videos son las más populares en términos de vistas, likes y comentarios?
2. ¿Existen patrones temporales en la popularidad de las distintas categorías de videos?
3. ¿Cómo influyen los metadatos (títulos, descripciones, tags) en la performance de los videos?
4. ¿Qué factores están asociados con un mayor nivel de interacción (likes y comentarios) en los videos?
5. ¿Cómo ha cambiado el volumen de los videos en tendencia a lo largo del tiempo?
6. ¿Qué canales de YouTube son tendencia más frecuentemente? ¿Y cuáles con menos frecuencia?
7. ¿En qué Estados se presenta el mayor número de “Vistas”, “Me gusta” y “No me gusta”?
8. ¿Es factible predecir el número de “Vistas” o “Me gusta” o “No me gusta”?
9. ¿Los videos en tendencia son los que mayor cantidad de comentarios positivos reciben?

### 2. Comprensión de los Datos
Para llevar a cabo este análisis, se utilizó un conjunto de datos proporcionado por YouTube, el cual contiene información sobre videos subidos en el mes de enero de 2021. Los datos incluyen varias características relevantes que se utilizarán para el análisis.

#### Descripción del Conjunto de Datos
El conjunto de datos original se encuentra en un archivo CSV titulado `INvideos_cc50_202101.csv`. Este archivo incluye información detallada sobre cada video, con las siguientes columnas principales:
- `video_id`: Identificador único de cada video.
- `trending_date`: Fecha en que el video comenzó a ser tendencia.
- `title`: Título del video.
- `channel_title`: Nombre del canal que subió el video.
- `category_id`: Identificador de la categoría del video.
- `publish_time`: Fecha y hora en que el video fue subido.
- `tags`: Palabras clave asociadas al video.
- `views`: Número de vistas del video.
- `likes`: Número de likes del video.
- `dislikes`: Número de dislikes del video.
- `comment_count`: Número de comentarios en el video.
- `thumbnail_link`: Enlace a la miniatura del video.
- `comments_disabled`: Indicador de si los comentarios están deshabilitados.
- `ratings_disabled`: Indicador de si las calificaciones están deshabilitadas.
- `video_error_or_removed`: Indicador de si el video ha sido eliminado o tiene un error.
- `description`: Descripción del video.

#### Metadatos de Categorías de Video
Además, se dispone de un archivo JSON que contiene las categorías de vídeo y sus respectivos identificadores. Este archivo proporciona un mapeo entre los `category_id` y los nombres de las categorías, permitiendo una interpretación más clara de los datos.

### 3. Preparación de los Datos
La preparación de los datos incluyó:
- Limpieza de Datos: Eliminación de duplicados y manejo de valores faltantes.
- Enriquecimiento de Datos: Creación de nuevas variables como `likes_per_view` y `comment_per_view` para una mejor comparabilidad entre videos.
- Clasificación: Asignación de videos a categorías específicas basadas en el JSON proporcionado.

#### Preprocesamiento
- Conversión de fechas: Las fechas en `trending_date` y `publish_time` fueron convertidas a objetos de tipo fecha.
- Conversión de columnas numéricas: Las columnas `views`, `likes`, `dislikes`, `comment_count`, `category_id`, `lat` y `lon` fueron convertidas a valores numéricos.

### 4. Modelado y Evaluación de Resultados
Se realizaron análisis descriptivos y visualizaciones para identificar patrones en los datos. A continuación, se presentan algunos de los resultados clave:

#### Distribución de Vistas
- La categoría "Music" muestra una media de vistas significativamente más alta en comparación con otras categorías.

#### Likes y Comentarios
- Las categorías como "Comedy" y "Entertainment" tienden a tener una alta proporción de likes y comentarios por vista.

### 5. Conclusiones
- Los resultados indican que ciertas categorías de videos tienen un mayor potencial para atraer vistas y generar interacciones. Estos insights pueden ser valiosos para los creadores de contenido al planificar sus estrategias de publicación.
- Después de analizar la volatilidad en el cambio de volumen de vídeos en tendencia, es prudente afirmar que un promedio similar puede presentarse en los posteriores años.
- Es interesante ver como la cantidad de caracteres tanto en el título, como en la descripción y en las etiquetas de los vídeos afectan en la visibilidad e interacción de los videos, lo cual podría sugerir que YouTube beneficia a aquellos videos con una cierta cantidad de caracteres en sus metadatos.
- El flujo de trabajo al modelar y revisar los modelos, recuerda mucho al de la metodología cualitativa, donde muchas veces tenemos que retrotraernos a pasos anteriores del análisis para obtener cambios en la precisión o varianza de los modelos propuestos.


## Instalación
Para ejecutar este proyecto, primero clona el repositorio y luego instala las dependencias necesarias:

```bash
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
pip install -r requirements.txt
```


## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cualquier cambio.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

---

Este README proporciona una visión general del proyecto y cómo usarlo. Si necesitas más detalles, consulta los notebooks y scripts proporcionados en el repositorio.