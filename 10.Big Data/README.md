# BIG DATA

A continuación, se detallan las tecnologías y herramientas más relevantes según su función:
### 1. Frameworks de Procesamiento y Almacenamiento
   - Apache Hadoop: Es el pilar del Big Data. Permite el procesamiento distribuido de grandes conjuntos de datos en clústeres de computadoras. Utiliza HDFS para el almacenamiento y MapReduce para el procesamiento.

   - **[Apache Spark](spark.ipynb)**: Conocido por su velocidad, procesa datos in-memory, lo que lo hace mucho más rápido que Hadoop para tareas iterativas y análisis en tiempo real.

   - Apache Flink: Ideal para el procesamiento de flujos de datos (streaming) en tiempo real con alta disponibilidad y precisión. 

### 2. Bases de Datos NoSQL

Diseñadas para manejar datos no estructurados y semiestructurados (como videos, redes sociales o sensores) con alta escalabilidad. 
   - **[MongoDB](mongoDB.md)**: Almacenamiento orientado a documentos.
Cassandra: Diseñada por Facebook para manejar grandes cantidades de datos distribuidos en muchos servidores.

   - HBase: Base de datos distribuida y escalable que corre sobre HDFS. 

### 3. Ingesta y Mensajería de Datos
   - Apache Kafka: Plataforma de transmisión de eventos que permite publicar, almacenar y procesar flujos de registros en tiempo real.

   - Apache Flume & Sqoop: Herramientas especializadas en la carga de datos masivos hacia el ecosistema Hadoop. 

### 4. Análisis y Visualización 
   - Lenguajes de programación: Python y R son los más utilizados por su amplia variedad de bibliotecas para análisis estadístico y Machine Learning.

   - Herramientas de consulta: Hive y Pig permiten realizar consultas sobre datos almacenados en Hadoop utilizando lenguajes similares a SQL.

   - Visualización: Herramientas como Tableau o Power BI ayudan a transformar datos complejos en gráficos e informes comprensibles. 
   
### 5. Soluciones en la Nube

Muchos de estos servicios se ofrecen de forma gestionada a través de plataformas como: 
   - Amazon Web Services (AWS) (ej. Amazon EMR, Redshift).
   - Google Cloud Platform (GCP) (ej. BigQuery).
   - Microsoft Azure (ej. Azure Data Lake, HDInsight).