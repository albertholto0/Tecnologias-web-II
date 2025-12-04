import React, { useState } from 'react';
import './App.css';

function App() {
  const [tareas, setTareas] = useState([]);
  const [texto, setTexto] = useState('');

  return (
    <div>
      <h1>Tareas</h1>
    </div>
  );
}

export default App;