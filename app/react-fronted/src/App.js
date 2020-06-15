import React, { Component } from 'react'
import { BrowserRouter as Router, Redirect, Switch } from 'react-router-dom';

import './assets/styles/index.scss';

import { Identifier, Btn, Image } from './components';

function App() {
  return (
    <div className="App">
      <Image/>
      <Identifier/>
      <Btn/>
    </div>
  );
}

export default App;