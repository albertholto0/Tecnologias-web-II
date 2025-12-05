import React from 'react';

function Tarea({ tarea, marcarCompletada, eliminarTarea }) {
  return (
    <div>
      <input 
        type="checkbox" 
        checked={tarea.completada}
        onChange={() => marcarCompletada(tarea.id)}
      />
      <span style={{ textDecoration: tarea.completada ? 'line-through' : 'none' }}>
        {tarea.texto}
      </span>
      <button onClick={() => eliminarTarea(tarea.id)}>
        Eliminar
      </button>
    </div>
  );
}

export default Tarea;