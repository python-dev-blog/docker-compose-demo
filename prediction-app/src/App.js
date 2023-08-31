import React from 'react';
import './App.css';
import PredictionButton from './components/PredictionButton';

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <PredictionButton />
      </header>
    </div>
  );
}

export default App;