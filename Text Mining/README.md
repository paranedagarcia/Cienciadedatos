
# Text Analysis


### 1.1 Definiciones
- **Text Mining**: Extracción de información estructurada de textos no estructurados mediante técnicas computacionales.
- **Procesamiento de Lenguaje Natural (PLN)**: Rama de la inteligencia artificial que facilita la interacción entre máquinas y lenguaje humano.

### 1.2 Relevancia
- Análisis de sentimientos en redes sociales
- Clasificación automática de documentos
- Extracción de entidades y relaciones
- Sistemas de recomendación basados en contenido

## 2. Fundamentos Teóricos

### 2.1 Pipeline de PLN
```
Texto Raw → Tokenización → Limpieza → Normalización → Análisis → Extracción
```

La preparación de datos en PLN exige una gestión técnica meticulosa estructurada en fases críticas:

- **Ingesta y Estructuración**: Se emplean objetos Dataset (basados en Apache Arrow) por su eficiencia en memoria. Estos se integran con Pandas para permitir la conversión a DataFrame, facilitando el análisis exploratorio mediante APIs de alto nivel.

- **Tokenización**: La elección entre tokenización por palabras o subpalabras (como Byte Pair Encoding o BPE) es determinante para la eficiencia del modelo. Un vocabulario basado exclusivamente en palabras únicas puede sufrir una explosión de parámetros: si se consideran 1 millón de palabras únicas proyectadas a vectores de 1.000 dimensiones, la matriz de pesos resultante contendría 1.000 millones de pesos, una cifra comparable a la totalidad de parámetros de un modelo GPT-2.

- **Normalización**: Técnicas como el stemming o la lematización reducen la variabilidad léxica al normalizar las palabras a su raíz, aunque implican un compromiso técnico debido a la pérdida de matices gramaticales y contextuales.

- **Aálisis**:

- **Extracción**:


### 2.2 Técnicas Fundamentales

#### **Tokenización** 
División en palabras/frases. La elección entre tokenización por palabras o subpalabras (como Byte Pair Encoding o BPE) es determinante para la eficiencia del modelo. Un vocabulario basado exclusivamente en palabras únicas puede sufrir una explosión de parámetros: si se consideran 1 millón de palabras únicas proyectadas a vectores de 1.000 dimensiones, la matriz de pesos resultante contendría 1.000 millones de pesos, una cifra comparable a la totalidad de parámetros de un modelo GPT-2.

Existen tres enfoques principales dependiendo de la granularidad requerida para la tarea:

• **Tokenización por palabras**: Es el método más común, donde el texto se segmenta generalmente utilizando los espacios en blanco como delimitadores. Aunque es intuitivo, puede generar vocabularios masivamente grandes y presenta dificultades con palabras raras o desconocidas (problema de out-of-vocabulary).

• **Tokenización por caracteres**: Divide el texto en letras individuales. Este enfoque reduce drásticamente el tamaño del vocabulario y evita problemas con palabras desconocidas, pero obliga al modelo a aprender la estructura de las palabras y la ortografía desde cero, lo cual es computacionalmente costoso.

• **Tokenización por subpalabras**: Representa el estándar actual para modelos avanzados como BERT o GPT. Combina los beneficios de los métodos anteriores al mantener palabras frecuentes como unidades únicas y dividir palabras raras o complejas en fragmentos menores (como "token" y "##izing"). Esto permite al modelo capturar significados de prefijos y sufijos de manera eficiente.

**Desafíos del Proceso**

La tokenización no es una simple división por espacios, ya que enfrenta varios obstáculos lingüísticos:

• **Contracciones y puntuación**: Determinar si una puntuación es el final de una frase o parte de una abreviatura (como "U.S.") o cómo dividir contracciones (como "don't" en "do" y "n't") requiere reglas complejas.

• **Idiomas sin espacios**: En lenguas como el chino o el japonés, donde no existen espacios entre palabras, se requieren segmentadores especializados para identificar las unidades léxicas.

• **Texto ruidoso**: En contextos como redes sociales o registros clínicos, el uso de jerga, emoticonos, errores ortográficos y acrónimos no estándar hace que la tokenización sea una tarea mucho más difícil.

**Herramientas y Bibliotecas en Python**

Hay tres bibliotecas principales para implementar este proceso:

• **NLTK (Natural Language Toolkit):** Proporciona funciones clásicas como word_tokenize y sent_tokenize, utilizando modelos entrenados como el de Penn Treebank para manejar contracciones y puntuación.

• **spaCy**: Ofrece un procesamiento industrial muy rápido y preciso que maneja la tokenización automáticamente como la primera etapa de su "pipeline", asignando además metadatos como la categoría gramatical a cada token.

• **Hugging Face (tokenizers)**: Diseñada específicamente para el aprendizaje profundo, está escrita en Rust para ofrecer una velocidad extrema y maneja algoritmos modernos de subpalabras como Byte-Pair Encoding (BPE) y WordPiece.

En resumen, la tokenización transforma el lenguaje humano desestructurado en una secuencia estructurada de vectores numéricos (a través de capas de embedding), permitiendo que los modelos matemáticos realicen tareas complejas como clasificación de texto, traducción automática o generación de respuestas.

**Tokenizacion en BERT y GPT**

Tanto **BERT** como **GPT** utilizan técnicas de **tokenización de subpalabras**, un enfoque intermedio entre la tokenización por caracteres y por palabras que permite manejar vocabularios grandes y evitar el problema de las palabras desconocidas (OOV). Sin embargo, implementan algoritmos diferentes para lograrlo:

#### 1. BERT y WordPiece
BERT (y sus variantes como DistilBERT) utiliza el algoritmo **WordPiece**.
*   **Mecanismo:** WordPiece segmenta las palabras en unidades menores cuando estas no son frecuentes en el corpus. Por ejemplo, una palabra compleja como "tokenizing" puede dividirse en `['token', '##izing']`.

*   **Identificación de continuación:** Utiliza el prefijo **`##`** para indicar que un token es la continuación de una palabra y que no debe haber un espacio delante de él al reconstruir el texto.

*   **Tokens especiales:** BERT añade tokens estructurales como **`[CLS]`** al inicio de la secuencia (usado para tareas de clasificación) y **`[SEP]`** para separar frases o marcar el final.

#### 2. GPT y Byte-Pair Encoding (BPE)
La familia GPT (especialmente GPT-2 y GPT-3) utiliza el algoritmo **Byte-Pair Encoding (BPE)**.
*   **Mecanismo:** BPE comienza con una base de caracteres individuales y fusiona iterativamente los pares de tokens más frecuentes para crear nuevas unidades.

*   **Nivel de bytes:** GPT-2 implementa una versión de **nivel de bytes** (byte-level BPE), que mapea los 256 valores posibles de un byte a caracteres Unicode imprimibles. Esto permite al modelo procesar cualquier cadena de texto sin generar nunca un token de "palabra desconocida", ya que cualquier carácter puede descomponerse en sus bytes base.

*   **Preservación de estructura:** A diferencia de WordPiece, BPE en GPT-2 suele incluir el espacio dentro del propio token. Utiliza símbolos visuales especiales en su representación interna, como **`Ġ`** para representar un espacio y **`Ċ`** para saltos de línea, permitiendo conservar la indentación y el formato original.

#### Comparación de beneficios
*   **Eficiencia de vocabulario:** Ambos métodos permiten representar un lenguaje complejo con un vocabulario de tamaño manejable (típicamente entre 30,000 y 50,000 tokens), lo que reduce la carga computacional en las capas de *embedding*.

*   **Generalización:** Al basarse en subunidades (como sufijos o raíces), los modelos pueden inferir el significado de palabras nuevas; por ejemplo, si el modelo conoce "fastest" y "smart", puede procesar mejor la palabra "smartest" aunque no la haya visto antes.

*   **Contextualización:** Estas técnicas de subpalabras alimentan las capas posteriores del Transformer, permitiendo que BERT genere representaciones bidireccionales y GPT genere texto de forma autorregresiva.

#### **Stemming/Lemmatización** 
Reducción a raíces

#### **Part-of-Speech Tagging**: 
Etiquetado morfosintáctico

#### **Named Entity Recognition (NER)**
Identificación de entidades

## 3. Ecosistema Python

### 3.1 Bibliotecas Principales
| Biblioteca | Propósito |
|-----------|----------|
| **NLTK** | Suite completa PLN clásico |
| **spaCy** | Procesamiento industrial, eficiente |
| **TextBlob** | Análisis de sentimientos simplificado |
| **Gensim** | Modelado de tópicos y Word2Vec |
| **Transformers (HuggingFace)** | Modelos BERT, GPT modernos |

### 3.2 Ejemplo: Análisis Básico con spaCy
```python
import spacy

nlp = spacy.load("es_core_news_sm")
doc = nlp("El análisis de textos es fundamental.")

for token in doc:
    print(f"{token.text} → {token.pos_}")
```

## 4. Aplicaciones Prácticas

- Análisis de sentimientos
- Clasificación temática
- Extracción de información
- Sistemas de búsqueda semántica

## 5. Conclusiones

Python proporciona un ecosistema maduro y robusto para Text Mining y PLN, permitiendo desde análisis clásicos hasta implementaciones de deep learning.

---
**Referencias**: Bird, Klein & Loper (2009). Natural Language Processing with Python.
