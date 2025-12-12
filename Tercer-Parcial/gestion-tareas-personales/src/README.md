# Gestion de Tareas Personales

Aplicacion web desarrollada en React para gestionar tareas personales de manera eficiente.

## Descripcion

Esta aplicacion permite a los usuarios crear, organizar y administrar sus tareas diarias. Incluye funcionalidades para agregar tareas con texto, fecha y hora opcionales, marcar tareas como completadas, visualizar tareas pendientes y completadas por separado, y eliminar tareas.

## Tecnologias Utilizadas

- React
- JavaScript
- CSS
- Bootstrap 5.3
- Google Fonts (Inter)

## Funcionalidades

### Agregar Tareas

- Permite agregar tareas con un minimo de 3 letras y maximo de 150 caracteres.
- No se puede agregar una tarea sin texto.
- Se puede agregar una fecha opcional utilizando un campo de tipo date.
- Se puede agregar una hora opcional utilizando un campo de tipo time.
- Es posible agregar tareas sin fecha ni hora.

### Validaciones

- Muestra alertas personalizadas cuando se intenta agregar una tarea vacia.
- Valida que la tarea tenga al menos 3 letras.
- Valida que la tarea no exceda los 150 caracteres.
- Muestra una alerta de exito cuando la tarea se agrega correctamente.

### Visualizacion de Tareas

- Las tareas se organizan en dos listas: Pendientes y Completadas.
- Solo se muestra la fecha y hora en las tareas que las tienen asignadas.
- Incluye contadores que muestran el numero de tareas pendientes.
- Incluye contadores que muestran el numero de tareas realizadas.

### Gestion de Tareas

- Permite marcar tareas como completadas mediante un checkbox.
- Las tareas completadas se muestran tachadas.
- Permite desmarcar tareas completadas para regresarlas a pendientes.
- Permite eliminar cualquier tarea de forma permanente.

## Estructura del Proyecto

```
src/
├── App.js                    # Componente principal
├── App.css                   # Estilos globales
├── componentes/
│   ├── FormularioTarea.js    # Formulario para agregar tareas
│   ├── ListaTareas.js        # Lista de tareas
│   └── Tarea.js              # Componente individual de tarea
``````

## Captura de Pantalla

![Aplicacion de Gestion de Tareas](/gestion-tareas-personales/public/capturas_pantalla/final.png)
