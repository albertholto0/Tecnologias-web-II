import React from 'react';

function Tarea({ tarea, marcarCompletada, eliminarTarea }) {
  return (
    <div className="list-group-item d-flex justify-content-between align-items-center">
      <div className="form-check">
        <input 
          className="form-check-input" 
          type="checkbox" 
          checked={tarea.completada}
          onChange={() => marcarCompletada(tarea.id)}
        />
        <label 
          className={`form-check-label ms-2 ${tarea.completada ? 'text-decoration-line-through text-muted' : ''}`}
        >
          {tarea.texto}
        </label>
      </div>
      <button 
        className="btn btn-sm btn-danger"
        onClick={() => eliminarTarea(tarea.id)}
      >
        Eliminar
      </button>
    </div>
  );
}

export default Tarea;