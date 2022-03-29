import { useState, useEffect } from 'react'
import './App.css';

function App() {

  const [words, setWords] = useState(null)


  
  useEffect(() => {
    fetch('/hello').then(res => {res.json().then(data => console.log(data.data))}).catch(err => console.log(err))
  }, [])



  return (
    <div className="App">
      {words}
      <input onChange={e => setWords(e.target.value)} />
      <button onClick={() => {
        fetch('/add-admin/'+words).then(res => console.log(res))
      }
      } >Click</button>
    </div>
  );
}

export default App;
