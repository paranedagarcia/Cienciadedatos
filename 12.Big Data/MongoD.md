<center><img src="../images/mongodb.png" width="600"></center>

# MongoDB

## Introducción

## Arquitectura
### Base de Datos
### Colecciones
Es la homologación a las tablas en las bases de datos relacionales. Agrupa un conjunto de documentos que son asimilables a los registros.

### Documentos
El documento se asemeja a los registros de una base tradicional. Sin embargo, estos estan constituidos por pares de clave/valor. Donde el valor puede ser ser de cualquier tipo: un número, arreglo, cadena de texto e inclusive otro documento. 

Cada documento está estructurado en un formato JSON (Javascript System Object Notation), del tipo:
```
{
    _id: ObjectId('67e17478507575ae54544')
    nombre: "Pedro",
    apellido: "Gonzalez Muñoz",
    edad: 45,
    activo: true,
    nacimiento: "1984-12-20",
    grupos: ["usuario", "editor", "autor"],
    correo: {
        personal: "pedrogonzalez@gmail.com",
        trabajo: "pedrogonza@ipp.cl"
    },
    telefono: {
        fijo: "+56278904566",
        celular: "+569807600",
        otro: "+56267891234"
    }
}
```

## Herramientas

### Compass
Es un aplicación de interface gráfica para interactuar con las bases de datos de MongoDB.

### Terminal SSH

## Referencias:
- Curso de MongoDB desde Cero: https://www.youtube.com/watch?v=rcZlFmioTkE
- MongoDb en una hora: https://www.youtube.com/watch?v=YyfdOX-Clf4


## Operaciones CRUD


## Consultas avanzadas


## Manejo de índices