/* Esto es un componente reutilizable, que se usa 
  por cada tarea que tenemos en nuestra lista (ListaTareas.js). */
function Tarea({ tarea, marcarCompletada, eliminarTarea }) {
  return (
    <div className="list-group-item d-flex justify-content-between align-items-center">
      <div className="form-check">
        {/* Es un manejador de eventos, que permite cambiar el estado de la tarea */}
        <input 
          className="form-check-input" 
          type="checkbox" 
          checked={tarea.completada}
          onChange={() => marcarCompletada(tarea.id)}
        />
        {/* Si la tarea esta completada, se muestra de manera tachada */}
        <label 
          className={`form-check-label ms-2 ${tarea.completada ? 'text-decoration-line-through text-muted' : ''}`}
        >
          {tarea.texto}
          {/* Si la tarea tiene fecha, se muestra la fecha y la hora */}
          {tarea.fecha && (
            <small className="d-block text-muted">
              {tarea.fecha} {tarea.hora}
            </small>
          )}
          {/* Si no tiene fecha pero si hora, solo se muestra la hora */}
          {!tarea.fecha && tarea.hora && (
            <small className="d-block text-muted">
              {tarea.hora}
            </small>
          )}
          {/* Si no tiene ni fecha ni hora, pues no se muestra nada */}
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

// exportamos el componente para usarlo en otros archivos
export default Tarea;