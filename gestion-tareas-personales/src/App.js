import React, { useState } from 'react';
import './App.css';
import FormularioTarea from './componentes/FormularioTarea';
import ListaTareas from './componentes/ListaTareas';

function App() {
  const [tareas, setTareas] = useState([]);

  const agregarTarea = (textoTarea) => {
    const palabras = textoTarea.trim().split(' ').filter(p => p.length > 0);
    
    if (textoTarea.trim() === '') {
      alert('No puedes agregar una tarea vacía');
      return;
    }
    
    if (palabras.length < 3) {
      alert('La tarea debe tener al menos 3 palabras');
      return;
    }
    
    if (textoTarea.length > 150) {
      alert('La tarea no puede tener más de 150 caracteres');
      return;
    }

    const nuevaTarea = {
      id: Date.now(),
      texto: textoTarea,
      completada: false
    };

    setTareas([...tareas, nuevaTarea]);
  };

  const marcarCompletada = (id) => {
    setTareas(tareas.map(tarea => 
      tarea.id === id ? { ...tarea, completada: !tarea.completada } : tarea
    ));
  };

  const eliminarTarea = (id) => {
    setTareas(tareas.filter(tarea => tarea.id !== id));
  };

  const tareasPendientes = tareas.filter(tarea => !tarea.completada);
  const tareasCompletadas = tareas.filter(tarea => tarea.completada);

  return (
    <div className="container">
      <h1 className="text-center my-4">Gestión de Tareas Personales</h1>
      <div className="text-center mb-4">
        <img src="/_.jpeg" alt="Gestión de tareas" style={{ maxWidth: '300px', width: '100%' }} />
      </div>
      
      <FormularioTarea agregarTarea={agregarTarea} />
      
      <div className="mt-4">
        <h3>Tareas Pendientes ({tareasPendientes.length})</h3>
        <ListaTareas 
          tareas={tareasPendientes} 
          marcarCompletada={marcarCompletada}
          eliminarTarea={eliminarTarea}
        />
      </div>

      {tareasCompletadas.length > 0 && (
        <div className="mt-4">
          <h3>Tareas Completadas ({tareasCompletadas.length})</h3>
          <ListaTareas 
            tareas={tareasCompletadas} 
            marcarCompletada={marcarCompletada}
            eliminarTarea={eliminarTarea}
          />
        </div>
      )}
    </div>
  );
}

export default App;