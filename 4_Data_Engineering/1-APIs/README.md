# Diseño de APIs: Buenas Prácticas y Ejemplos

En el desarrollo de APIs es fundamental garantizar que su diseño sea intuitivo, consistente y escalable. Un buen diseño no solo facilita la integración y el mantenimiento, sino que también mejora la experiencia de los desarrolladores que las utilizan. En este material abordaremos los principios básicos, ejemplos de naming adecuado e inadecuado, y recomendaciones adicionales para la creación de APIs robustas.

---

## 1. Introducción

Las APIs permiten la comunicación entre sistemas y, por ello, deben ser diseñadas como recursos claros y bien definidos. Es importante que los endpoints reflejen la lógica del dominio de la aplicación y no la estructura interna de la base de datos. Esto permite una mayor flexibilidad y evita exponer detalles internos innecesarios.

---

## 2. Principios Básicos para el Diseño de APIs

- **Recursos como Sustantivos:**  
  Utiliza sustantivos en plural para representar recursos (ej. `/empleados`, `/departamentos`).

- **Acciones a través de Métodos HTTP:**  
  No es necesario incluir verbos en la URL. Las operaciones se definen con los métodos HTTP:  
  - `GET` para recuperar datos  
  - `POST` para crear nuevos registros  
  - `PUT` o `PATCH` para actualizar  
  - `DELETE` para eliminar

- **Consistencia y Simplicidad:**  
  Los endpoints deben ser fáciles de entender y utilizar, evitando ambigüedades y excesiva complejidad en la nomenclatura.

- **Jerarquía y Relaciones:**  
  Representa las relaciones entre recursos de manera lógica, utilizando rutas anidadas cuando corresponda.

---

## 3. Ejemplos de Buen Naming ✅

A continuación, se presentan ejemplos de endpoints bien diseñados:

- `/empleados`  
- `/departamentos`  
- `/empleados/9e0343b9-a873-4db7-813e-fdeb68305d3b/departamentos`  
- `/candidatos/busqueda?nombre=jhon&pagina=1&limite=20`

### ¿Por qué son buenos?

- **`/empleados`:**  
  Este endpoint se utiliza para crear o actualizar un empleado individual, o incluso para recuperar toda la colección.

- **`/departamentos`:**  
  De manera similar, se utiliza para gestionar los departamentos.

- **`/empleados/{id}/departamentos`:**  
  Permite actualizar o recuperar los departamentos asociados a un empleado específico.

- **`/candidatos/busqueda`:**  
  Sigue una semántica clara para realizar búsquedas. Los parámetros de consulta (`nombre`, `pagina`, `limite`) permiten filtrar y paginar los resultados de forma precisa.

---

## 4. Ejemplos de Mal Naming ❌

Evita los siguientes patrones en tus endpoints:

- **`/empleado`:**  
  No usar el plural genera inconsistencia.

- **`/departamentos/crear`:**  
  La acción de crear debe definirse mediante el método HTTP (`POST`), no en la URL.

- **`/obtenerEmpleadoPorId`:**  
  Incluir prefijos como "get" es redundante, ya que el método HTTP ya indica la acción.

- **`/busqueda?tipo=candidato&nombre=jhon&pagina=1&limite=20`:**  
  Evita utilizar flags o indicadores que compliquen la semántica del endpoint. Es preferible definir rutas que representen directamente el recurso que se está buscando.

---

## 5. Consideraciones Avanzadas

### 5.1. Endpoints como Representación de Recursos

- **Abstracción de la Fuente de Datos:**  
  Los endpoints deben reflejar recursos de negocio y no las tablas o estructuras internas de la base de datos.  
  **Ejemplo:**  
  Si tienes tablas como `VEHICLE`, `CAR`, `BIKE`, `PIECE`, en lugar de crear un endpoint para cada tabla, define endpoints que representen recursos relevantes para el dominio:
  - Correcto:  
    - `/autos` y `/motos` para diferenciar tipos de vehículos.
    - `/autos/piezas` y `/motos/piezas` para gestionar piezas asociadas.
    - `/autos/{id}/piezas` para consultar las piezas de un modelo específico.
  
  - Incorrecto:
    - `/vehiculos`
    - `/cars`
    - `/bikes`
    - `/pieces`

### 5.2. Uso de Métodos HTTP

La acción se determina por el método HTTP, no por el nombre del endpoint:

- `GET /empleados` → Recuperar la lista de empleados.
- `POST /empleados` → Crear un nuevo empleado.
- `PUT /empleados/{id}` → Actualizar un empleado existente.
- `DELETE /empleados/{id}` → Eliminar un empleado.

### 5.3. Versionado de la API

Para evitar rupturas en la compatibilidad, es aconsejable versionar la API:

- Ejemplo: `/v1/empleados`  
  Esto permite introducir cambios y mejoras sin afectar a los clientes que usan versiones anteriores.

### 5.4. Documentación y Comunicación

- **Documentación:**  
  Una API bien documentada facilita su adopción y uso. Herramientas como Swagger, OpenAPI o Postman pueden ser muy útiles para generar y mantener documentación actualizada.

- **Manejo de Errores:**  
  Implementa respuestas claras y consistentes para errores. Un buen manejo de errores mejora la experiencia del usuario y facilita la depuración.

- **Seguridad:**  
  Asegura la API mediante autenticación, autorización y cifrado de datos. Es crucial proteger la información sensible y limitar el acceso a recursos.

---

## 6. Conclusión

El diseño de APIs es un aspecto fundamental en la construcción de sistemas robustos y escalables. Al seguir estos lineamientos y buenas prácticas, se logra:

- Una mayor claridad y consistencia en la estructura de los endpoints.
- Una mejor abstracción de la lógica del negocio respecto a la fuente de datos.
- Una API fácil de consumir y mantener, lo que facilita la integración con otros sistemas.

