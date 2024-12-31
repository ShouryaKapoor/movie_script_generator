import React from 'react';
import './styles/App.css';
import ScriptGenerator from './components/ScriptGenerator';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Movie Script Generator</h1>
      </header>
      <main>
        <ScriptGenerator />
      </main>
    </div>
  );
}

export default App;