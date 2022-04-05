import { useState } from 'react'
import './App.css'
import LoginRegister from './components/LoginRegister'
import ViewerStats from './components/ViewerStats'

function App() {

  const [page, setPage] = useState("LoginRegister")

  return (
    <div className="App">
      <button onClick={() => setPage("LoginRegister")}>Login Register Page</button>
      <button onClick={() => setPage("ViewerStats")}>Viewer Stats</button>
      { page === "LoginRegister" ? <LoginRegister /> : null }
      { page === "ViewerStats" ? <ViewerStats /> : null }
    </div>
  );
}

export default App;
