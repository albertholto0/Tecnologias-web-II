import React, { useState } from 'react';

function FormularioTarea({ agregarTarea }) {
  const [texto, setTexto] = useState('');

  const manejarEnvio = (e) => {
    e.preventDefault();
    agregarTarea(texto);
    setTexto('');
  };

  return (
    <form onSubmit={manejarEnvio}>
      <div>
        <label>Nueva Tarea</label>
        <input 
          type="text" 
          value={texto}
          onChange={(e) => setTexto(e.target.value)}
          placeholder="Escribe tu tarea aquí (mínimo 3 palabras, máximo 150 caracteres)"
        />
      </div>
      <button type="submit">Agregar Tarea</button>
    </form>
  );
}

export default FormularioTarea;