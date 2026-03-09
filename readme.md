## Ejecutar el entorno virtual

- Crear el entorno virtual: `py -3.12 -m venv venv`
- Activar el entorno virtual:
   
   En Windows: `.\venv\Scripts\activate`
   
   En Mac/Linux: `source venv/bin/activate`
   
- Instalar dependencias: `pip install -r requirements.txt`

## Instalar unittest

Este marco de trabajo viene instalado para su uso en python. Para comprobar su funcionamiento se puede ejecutar l siguiente instrucción:

`python -m unittest -h`

Primer bloque (ejecución directa): explica cómo pasar módulos, clases o métodos concretos al comando para correr sólo esos tests. Las opciones principales:

`-v / --verbose` aumenta el detalle del reporte, `-q / --quiet` lo reduce.

`--locals` muestra variables locales en los tracebacks, útil para depurar.

`--durations N` lista los N tests más lentos.

`-f / --failfast` se detiene en la primera falla.

`-c / --catch` captura Ctrl+C y muestra el estado hasta ese momento.

`-b / --buffer` suprime stdout/stderr de los tests salvo que fallen.

`-k PATTERN` filtra los nombres de test por un substring.

Luego da ejemplos para ejecutar un módulo, una clase, un método o un archivo específico.
Segundo bloque (unittest discover): igual que arriba, pero orientado al modo de descubrimiento automático. Las 

opciones adicionales:

`-s` el directorio inicial de búsqueda (por defecto .).

`-p` el patrón de archivo (por defecto test*.py).

`-t` el directorio raíz del proyecto para que los módulos se importen correctamente.

Recuerda que los módulos de test deben ser importables desde ese tope.

## Correr las pruebas con mayor nivel de detalle en los mensajes: Para lograr esto se utiliza la instrucción:

`python -m unittest -v tests/test_album.py`

## Ejecutar todas las pruebas de la carpeta tests: Se realiza al ejecutar

`python -m unittest discover -s tests -v`

NOTA: Para este tutorial y el resto de pruebas se recomienda utilizar este comando.

## Listar las opciones de unittest: Para obtener la ayuda de unittest se ejecuta la siguiente instrucción:

`python -m unittest -h`

## Los dos métodos principales para ejecutar las pruebas son:

`setUp():`

Es un método que se llama antes de llamar los métodos con las pruebas, se utiliza para preparar los objetos que se utilizarán en el conjunto de pruebas. Por defecto, su implementación no realiza acción alguna.

`tearDown():`

Es un método que se llama justo después de llamar la última instrucción en las pruebas y luego de guardar los resultados, y es generalmente utilizado para capturar las excepciones de los métodos con las pruebas para definir qué sucedió al ejecutarlas.


## Los métodos assert más utilizados según el sitio https://docs.python.org/3/library/unittest.html son los siguientes:


`assertEqual(a, b): Verifica que los argumentos ‘a' y ‘b' sean iguales`

`assertNotEqual(a, b): Verifica que los argumentos ‘a' y ‘b' sean diferentes`

`assertTrue(x): Verifica que el argumento ‘x' sea un valor verdadero. El argumento debe ser de tipo boolean`

`assertFalse(x): Verifica que el argumento ‘x' sea un valor falso. El argumento debe ser de tipo boolean`

`assertIs(a, b): Verifica que los argumentos ‘a' y ‘b' sean el mismo objeto`

`assertIsNot(a, b): Verifica que los argumentos ‘a' y ‘b' no sean el mismo objeto`

`assertIsNone(x): Verifica que el argumento ‘x' sea un valor None`

`assertIsNotNone(x): Verifica que el argumento ‘x' no sea un valor None`

`assertIn(a, b): Verifica que el elemento ‘a' se encuentre contenido en el contenedor o conjunto ‘b'. El elemento ‘b' debe ser un contenedor o conjunto`

`assertNotIn(a, b): Verifica que el elemento ‘a' no se encuentre contenido en el contenedor o conjunto ‘b'. El elemento ‘b' debe ser un contenedor o conjunto`

`assertIsInstance(a, b): Verifica que el objeto ‘a' sea una instancia de la clase ‘b'`

`assertNotIsInstance(a, b): Verifica que el objeto ‘a' no sea una instancia de la clase ‘b`