import { useState, useEffect } from 'react'
import './App.css';

function App() {

  const [words, setWords] = useState([])
  
  useEffect(() => {
    fetch('/hello').then(res => {res.json().then(data => setWords(data.data))}).catch(err => console.log(err))
  }, [])

  return (
    <div className="App">
      {words}
    </div>
  );
}

export default App;
