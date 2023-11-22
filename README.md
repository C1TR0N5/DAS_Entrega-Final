# DAS_Entrega-Final

Instructions for Unix-like systems

## Run
```console
python3 -m venv venv
```
```console
source venv/bin/activate
```
```console
pip install -r requirements.txt
```
```console
python src/main.py
```

### SOLID practices y Design Patterns
OCP (principio abierto/cerrado): las entidades de software deben estar abiertas a la extensión pero cerradas a la modificación. Esto significa que el comportamiento de un módulo se puede ampliar sin modificar su código fuente.

DIP (principio de inversión de dependencia): los módulos de alto nivel no deben depender de los módulos de bajo nivel; ambos deberían depender de abstracciones. Las abstracciones no deberían depender de detalles; los detalles deberían depender de abstracciones. Este principio tiene como objetivo reducir el acoplamiento directo entre diferentes módulos o clases para aumentar la modularidad y la flexibilidad.

SRP (Principio de Responsabilidad Única): Una clase o módulo debe tener una, y solo una, razón para cambiar, lo que significa que debe tener solo un trabajo o responsabilidad. Esto ayuda a crear una base de código más sólida, fácil de mantener y comprensible al garantizar que cada clase o módulo tenga la tarea de un único aspecto de la funcionalidad proporcionada por el software.

### ¿Cuales son el top 5 de caracteristicas de arquitectura del diseño actual de tu proyecto?
1. Usabilidad: Están implícitas rutas y funciones fáciles de usar, que agilizan el proceso para que los usuarios interactúen con el sistema, como agregar y eliminar elementos.
2. Mantenibilidad: la estructura del código del sistema, incluida la aplicación de los patrones Builder y Singleton, está orientada a facilitar la modificación y el mantenimiento.
3. Robustez: el manejo de errores está integrado dentro del sistema, particularmente en funciones como deleteItem y addItem, que administran excepciones para mantener la solidez.
4. Extensibilidad: el uso del patrón Builder en item_model.py facilita la adición de nuevas funciones, lo que permite una fácil expansión de las capacidades de la clase Item.
5. Confiabilidad: El sistema enfatiza la confiabilidad y la seguridad, como se ve en funciones como "addItem", que incluyen salvaguardas para la inserción de datos, destacando el compromiso con la integridad del sistema.

### Si la aplicacion migrara a una arquitectura de microservicios, ¿Cuales serian el top 5 de caracteristicas de arquitectura?
1. Mantenibilidad
2. Extensibilidad
3. Escalabilidad
4. Interoperabilidad
5. Confiabilidad