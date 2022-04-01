import { useState, useEffect } from 'react'
import './App.css';

function App() {

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')


  return (
    <div className="App">
      <div className='add-admin'>
        <h1>Add Admin</h1>
        <h2>Username:</h2>
        <input onChange={e => setUsername(e.target.value)} />
        <h2>Password:</h2>
        <input type="password" onChange={e => setPassword(e.target.value)} />

        <button onClick={() => {
          fetch('/add-admin/', {
            method: 'POST',
            body: JSON.stringify(
              {
                username: username,
                password: password
              }
            )
          })
          .then(res => res.json().then(data => console.log(data)))
        }
        } >Add Admin</button>
      </div>
      <div>
      </div>
    </div>
  );
}

export default App;
