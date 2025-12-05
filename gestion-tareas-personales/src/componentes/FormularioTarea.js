import React, { useState } from 'react';

function FormularioTarea({ agregarTarea }) {
  const [texto, setTexto] = useState('');

  const manejarEnvio = (e) => {
    e.preventDefault();
    agregarTarea(texto);
    setTexto('');
  };

  return (
    <form onSubmit={manejarEnvio} className="card p-3">
      <div className="mb-3">
        <label className="form-label">Nueva Tarea</label>
        <input 
          type="text" 
          className="form-control" 
          value={texto}
          onChange={(e) => setTexto(e.target.value)}
          placeholder="Escribe tu tarea aquí (mínimo 3 palabras, máximo 150 caracteres)"
        />
      </div>
      <button type="submit" className="btn btn-primary">Agregar Tarea</button>
    </form>
  );
}

export default FormularioTarea;