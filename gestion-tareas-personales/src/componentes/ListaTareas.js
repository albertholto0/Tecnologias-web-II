import Tarea from './Tarea';

function ListaTareas({ tareas, marcarCompletada, eliminarTarea }) {
  // RENDERIZADO CONDICIONAL
  // Si no hay nadota da tareas, muestra el siguiente mensaje
  if (tareas.length === 0) {
    return <p className="text-muted">No hay tareas</p>;
  }

  // Si si hay, pues continua con el renderizado de la lista de tareas
  return (
    <div className="list-group">
      
      {tareas.map(tarea => (
        <Tarea 
        // pasa una tarea individual al componente Tarea
          key={tarea.id}
          tarea={tarea}
          marcarCompletada={marcarCompletada}
          eliminarTarea={eliminarTarea}
        />
      ))}
    </div>
  );
}

// exportamos el componente para usarlo en otros archivos
export default ListaTareas;