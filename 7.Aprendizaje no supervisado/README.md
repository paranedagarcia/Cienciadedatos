# Machine Learning No Supervisado

El *machine learning no supervisado* es una rama de la inteligencia artificial donde los algoritmos analizan datos sin que les diga cuál es la respuesta correcta. Es decir, no se les da una "respuesta" o etiqueta previa, sino que el sistema debe encontrar patrones, similitudes o estructuras por sí mismo.

En términos simples, imagina que tienes una caja llena de botones de diferentes colores y tamaños, pero no sabes nada sobre ellos. El machine learning no supervisado sería como pedirle a una máquina que agrupe los botones según sus características, sin decirle cómo hacerlo. La máquina podría agruparlos por color, tamaño o forma, dependiendo de lo que encuentre en los datos.

**Ejemplos cotidianos:**
- **Agrupación de fotos:** Tu teléfono puede organizar automáticamente tus fotos en álbumes según las personas que aparecen, sin que tú le digas quién es quién.

- **Recomendaciones de música:** Plataformas como Spotify agrupan canciones similares para sugerirte listas de reproducción, aunque nunca hayas escuchado esas canciones antes.

- **Detección de fraudes:** Los bancos pueden identificar transacciones inusuales agrupando comportamientos similares y detectando los que se salen de lo común.

- **Segmentación de clientes:** Las empresas pueden dividir a sus clientes en grupos según sus hábitos de compra, para ofrecerles productos personalizados.

En resumen, el machine learning no supervisado ayuda a descubrir información oculta en los datos, encontrando patrones y agrupaciones que pueden ser útiles para tomar decisiones o entender mejor la información.

#### K-means

- **Propósito**: Agrupamiento (clustering).
- **Funcionamiento**: Particiona los datos en k grupos, minimizando la varianza intra-cluster (distancia entre puntos y el centroide del grupo).
- **Aplicaciones**: Segmentación de clientes, organización de documentos, análisis de imágenes.

[Ver Kmeans](K-Means.ipynb)

#### DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
- **Propósito**: Clustering basado en densidad.
- **Ventaja**: Detecta grupos de formas arbitrarias y es robusto frente a valores atípicos (outliers).
- **Aplicaciones**: Detección de fraudes, análisis geoespacial, identificación de anomalías.

[ver DBSCAN](DBSCAN.ipynb)

#### Análisis de componentes principales (PCA)

El análisis de componentes principales (PCA, por sus siglas en inglés) es una técnica que nos ayuda a simplificar datos complejos.
- **Propósito**: Visualización de datos de alta dimensión en 2D o 3D.
- **Característica**: Preserva la proximidad local entre puntos, útil para explorar agrupamientos complejos.
- **Aplicaciones**: Biología computacional, análisis de redes neuronales, exploración de datasets complejos.

[ver PCA](PCA.ipynb)

#### t-SNE (t-Distributed Stochastic Neighbor Embedding)
- **Propósito**: Visualización de datos de alta dimensión en 2D o 3D.
- **Característica**: Preserva la proximidad local entre puntos, útil para explorar agrupamientos complejos.
- **Aplicaciones**: Biología computacional, análisis de redes neuronales, exploración de datasets complejos.

#### Autoencoders
- **Propósito**: Aprendizaje de representaciones mediante redes neuronales.
- **Funcionamiento**: Codifican los datos en una representación comprimida y luego los reconstruyen.
- **Aplicaciones**: Detección de anomalías, eliminación de ruido en imágenes, compresión de datos.


### Aplicaciones cotidianas del Aprendizaje No Supervisado
El aprendizaje no supervisado tiene un impacto significativo en múltiples aspectos de la vida diaria, aunque muchas veces de manera transparente para el usuario final. Algunos ejemplos incluyen:

- **Recomendación de contenido**: Plataformas como Netflix o Spotify utilizan algoritmos de clustering para agrupar usuarios con preferencias similares y sugerir películas o canciones.

- **Segmentación de clientes**: Empresas de retail usan K-Means para identificar grupos de consumidores con comportamientos de compra similares y diseñar estrategias de marketing personalizadas.

- **Detección de fraudes**: Sistemas financieros aplican DBSCAN o autoencoders para identificar transacciones inusuales que se desvían del patrón normal.

- **Organización de archivos digitales**: Aplicaciones de fotos en teléfonos inteligentes agrupan imágenes por rostros o escenarios sin necesidad de etiquetas manuales.

- **Bioinformática**: Investigadores agrupan genes con expresión similar para descubrir funciones biológicas o enfermedades asociadas.