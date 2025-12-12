/* Componente principal de mi aplicación */
import React, { useState, useEffect } from 'react';
import './App.css';
import FormularioTarea from './componentes/FormularioTarea';
import ListaTareas from './componentes/ListaTareas';

function App() {
  const [tareas, setTareas] = useState([]); // Arreglo pa guardar las tareas
  const [alerta, setAlerta] = useState(''); // Texto del mensaje de alerta
  const [tipoAlerta, setTipoAlerta] = useState('warning'); 

  useEffect(() => {
    console.log("Las tareas han cambiado:", tareas);
  }, [tareas]);

  useEffect(() => {
    console.log("Componente App montado");
  }, []);

  const agregarTarea = (textoTarea, fecha, hora) => {
    // Valida que no sea una tarea vacia
    if (textoTarea.trim() === '') {
      setTipoAlerta('warning');
      setAlerta('No puedes agregar una tarea vacía');
      setTimeout(() => setAlerta(''), 3000);
      return;
    }
    // Valida que el texto este en rango de 3-150 caracteres
    if (textoTarea.trim().length < 3) {
      setTipoAlerta('warning');
      setAlerta('La tarea debe tener al menos 3 letras');
      setTimeout(() => setAlerta(''), 3000);
      return;
    }
    
    if (textoTarea.length > 150) {
      setTipoAlerta('warning');
      setAlerta('La tarea no puede tener más de 150 caracteres');
      setTimeout(() => setAlerta(''), 3000);
      return;
    }
    // Si ninguna validación falla, se agrega la tarea
    const nuevaTarea = {
      id: Date.now(),
      texto: textoTarea,
      fecha: fecha || null,
      hora: hora || null,
      completada: false
    };

    setTareas([...tareas, nuevaTarea]);
    setTipoAlerta('success');
    setAlerta('¡Tarea agregada!');
    setTimeout(() => setAlerta(''), 3000);
  };

  const marcarCompletada = (id) => {
    // Busca la tarea por id
    const tarea = tareas.find(t => t.id === id);
    if (tarea) {
      const nuevoEstado = !tarea.completada;
      if (nuevoEstado) {
        console.log(`Tarea completa: "${tarea.texto}"`);
      }
    }
    // Cambia el estado de completada de la tarea con el id dado
    setTareas(tareas.map(tarea => 
      tarea.id === id ? { ...tarea, completada: !tarea.completada } : tarea
    ));
    // recorre todas las tareas y cuando encuentra la que coincide con el id,
    // cambia su estado de completada a su opuesto (true a false o false a true)
  };

  const eliminarTarea = (id) => {
    // Elimina la tarea con el id dado
    setTareas(tareas.filter(tarea => tarea.id !== id));
  };
   // Separa las tareas en pendientes y completadas
  const tareasPendientes = tareas.filter(tarea => !tarea.completada);
  const tareasCompletadas = tareas.filter(tarea => tarea.completada);

  /*
    Se renderiza el titulo de la aplicación, así como la imagen.
    Las alertas, cuadro para agregar tareas, tareas pendientes y completadas
  */
  return (
    <div className="container">
      <h1 className="text-center my-4"><b>Gestión de Tareas Personales</b></h1>
      <div className="text-center mb-4">
        <img src="/_.jpeg" alt="Gestión de tareas" style={{ maxWidth: '250px', width: '100%' }} />
      </div>

      {alerta && (
        <div className={`alert alert-${tipoAlerta} alert-dismissible fade show`} role="alert">
          {alerta}
          <button type="button" className="btn-close" onClick={() => setAlerta('')}></button>
        </div>
      )}
      
      <FormularioTarea agregarTarea={agregarTarea} />
      
      <div className="mt-4">
        <h3>Tareas Pendientes ({tareasPendientes.length})</h3>
        <ListaTareas 
        // pasa las tareas pendientes al componente ListaTareas
          tareas={tareasPendientes} 
          // pasa las funciones para marcar como completada y eliminar tarea
          marcarCompletada={marcarCompletada}
          // pasa las funciones para marcar como completada y eliminar tarea
          eliminarTarea={eliminarTarea}
        />
      </div>
      {/* Aquí se muestran las tareas completadas */}
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

// exportamos el componente para usarlo en otros archivos
export default App;