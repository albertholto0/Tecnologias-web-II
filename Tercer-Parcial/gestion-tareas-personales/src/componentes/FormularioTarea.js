import React, { useState } from 'react';

// Funcion que biene desde App.js para agregar una tarea nueva
function FormularioTarea({ agregarTarea }) {
  const [texto, setTexto] = useState(''); // para guardar lo que el usuario ingrese en el "input"
  const [fecha, setFecha] = useState('');
  const [hora, setHora] = useState('');

  // Se ejecuta cuando le hago click al boton "Agregar Tarea"
  const manejarEnvio = (e) => {
    e.preventDefault();
    agregarTarea(texto, fecha, hora);
    setTexto('');
    setFecha('');
    setHora('');
  };

  // Se renderiza el cuadro para agregar mi tarea, 
  // con estilos de boostrap. 
  return (
    // Formulario para agregar tarea
    <form onSubmit={manejarEnvio} className="card p-3"> 
      <div className="mb-3">
        <label className="form-label">Nueva Tarea</label>
        <input 
          type="text" 
          className="form-control" 
          value={texto}
          // cada que el usuario escribe algo, se actualiza el estado "texto"
          onChange={(e) => setTexto(e.target.value)}
          placeholder="Escribe aquí (3 a 150 caracteres)"
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Fecha (opcional)</label>
        <input 
          type="date" 
          className="form-control" 
          value={fecha}
          // cada que el usuario escribe algo, se actualiza el estado "fecha"
          onChange={(e) => setFecha(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Hora (opcional)</label>
        <input 
          type="time" 
          className="form-control" 
          value={hora}
          // y cada que el usuario escribe algo, se actualiza el estado "hora"
          onChange={(e) => setHora(e.target.value)}
        />
      </div>
      <button type="submit" className="btn btn-primary">Agregar Tarea</button>
    </form>
  );
}
// aqui exportamos el componente para usarlo en otros archivos
export default FormularioTarea;