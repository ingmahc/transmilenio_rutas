# Sistema de Rutas de TransMilenio

Este proyecto fue desarrollado por **Miguel Ángel Herrera** para la clase de **Inteligencia Artificial** de la **Universidad Iberoamericana**. Su propósito es implementar un sistema basado en grafos que permita calcular la mejor ruta entre estaciones del sistema de transporte masivo TransMilenio.

---

## Descripción

El sistema utiliza la biblioteca **NetworkX** para modelar las estaciones y rutas como un grafo dirigido. Cada estación es un nodo, y las conexiones entre estaciones son aristas con atributos como tiempo y ruta. A partir de una estación de origen y una de destino, el programa calcula:

- La **ruta más corta** en tiempo.
- Los **detalles del trayecto**, como rutas utilizadas y tiempos estimados entre estaciones.

---

## Características

- Modela múltiples rutas de TransMilenio (C19, B23, D21, y otras) en un grafo único.
- Permite calcular la mejor ruta entre cualquier estación.
- Presenta detalles del trayecto, incluyendo tiempos y rutas específicas.
- Extensible para agregar nuevas rutas o datos.

---

## Requisitos

- **Python**: Versión 3.8 o superior.
- **Librerías**: NetworkX.

---

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/ingmahc/transmilenio_rutas.git
Navega al directorio del proyecto:

bash
Copiar código
cd transmilenio_rutas
Instala las dependencias necesarias:

bash
Copiar código
pip install -r requirements.txt
Uso
Ejecuta el archivo principal:

bash
Copiar código
python main.py
Ingresa la estación de origen y la estación de destino cuando se te solicite.

El programa mostrará:

La mejor ruta encontrada.
El tiempo estimado del trayecto.
Los detalles del recorrido, incluyendo las rutas utilizadas.
Ejemplo de Ejecución
plaintext
Copiar código
Bienvenido al sistema de rutas de TransMilenio.

Ingrese la estación de origen: Portal Sur
Ingrese la estación de destino: Portal Norte

La mejor ruta encontrada es:
 -> Portal Sur -> General Santander -> Calle 40 Sur -> Venecia -> Carrera 30 -> Ricaurte -> Calle 19 -> Calle 72 -> Calle 100 -> Portal Norte
Tiempo estimado: 47 minutos.

Detalles del trayecto:
- Portal Sur -> General Santander (Ruta: C19, Tiempo: 5 min)
- General Santander -> Calle 40 Sur (Ruta: C19, Tiempo: 4 min)
- Calle 40 Sur -> Venecia (Ruta: C19, Tiempo: 3 min)
- Venecia -> Carrera 30 (Ruta: C19, Tiempo: 6 min)
- Carrera 30 -> Ricaurte (Ruta: C19, Tiempo: 8 min)
- Ricaurte -> Calle 19 (Ruta: C19, Tiempo: 7 min)
- Calle 19 -> Calle 72 (Ruta: C19, Tiempo: 9 min)
- Calle 72 -> Calle 100 (Ruta: C19, Tiempo: 5 min)
- Calle 100 -> Portal Norte (Ruta: C19, Tiempo: 6 min)
Detalles de los Archivos
main.py: Archivo principal para ejecutar el programa.
rutas.py: Contiene las funciones y lógica del sistema de rutas (grafo y cálculos).
.gitignore: Archivo para ignorar archivos innecesarios en el repositorio, como entornos virtuales y archivos temporales.
requirements.txt: Lista de dependencias necesarias para ejecutar el proyecto.
README.md: Documentación del proyecto.
Posibles Mejoras
Ampliar las Rutas: Agregar todas las rutas y estaciones reales de TransMilenio.
Datos en Tiempo Real: Integrar una API para obtener tiempos actualizados y estado de las rutas.
Visualización de Rutas: Usar bibliotecas como folium o matplotlib para mostrar las rutas en un mapa.
Optimización: Mejorar el rendimiento al manejar sistemas de transporte más grandes.
Interfaz Gráfica: Implementar una interfaz de usuario para mejorar la experiencia.
Autor
Este proyecto fue desarrollado por:

Miguel Ángel Herrera
Estudiante de Inteligencia Artificial
Universidad Iberoamericana

Contacto
Si tienes preguntas, sugerencias o comentarios, puedes contactarme en:

Correo: ingmahc@gmail.com
GitHub: ingmahc
yaml
Copiar código

---

### **Instrucciones para Guardar y Subir**

1. Crea el archivo `README.md` en la raíz del proyecto.
2. Copia y pega el contenido del archivo anterior.
3. Guarda los cambios.
4. Súbelo al repositorio con los siguientes comandos en PowerShell:

   ```bash
   git add README.md
   git commit -m "Agregar README.md con detalles del proyecto"
   git push origin main
