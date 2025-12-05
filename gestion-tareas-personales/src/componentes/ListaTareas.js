import React from 'react';
import Tarea from './Tarea';

function ListaTareas({ tareas, marcarCompletada, eliminarTarea }) {
  if (tareas.length === 0) {
    return <p className="text-muted">No hay tareas</p>;
  }

  return (
    <div className="list-group">
      {tareas.map(tarea => (
        <Tarea 
          key={tarea.id}
          tarea={tarea}
          marcarCompletada={marcarCompletada}
          eliminarTarea={eliminarTarea}
        />
      ))}
    </div>
  );
}

export default ListaTareas;