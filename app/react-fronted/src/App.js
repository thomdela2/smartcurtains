// @ts-nocheck
import React from 'react';
import './assets/styles/index.scss';

import { Image, Identifier, Btn } from './components';

function App() {
  return (
    <div className="App">

  <p>{window.token}</p>
      <Image></Image>      
      <Btn></Btn>  
      <Identifier></Identifier>

    </div>
  );
}

export default App;
