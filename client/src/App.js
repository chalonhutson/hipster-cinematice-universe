import { useState } from 'react'
import './App.css'
import LoginRegister from './components/LoginRegister'
import ViewerStats from './components/ViewerStats'

function App() {

  const [page, setPage] = useState("LoginRegister")
  const [viewerId, setViewerId] = useState(7)

  return (
    <div className="App">
      <h1>Viewer Id = {viewerId}</h1>
      <button onClick={() => setPage("LoginRegister")}>Login Register Page</button>
      <button onClick={() => setPage("ViewerStats")}>Viewer Stats</button>
      { page === "LoginRegister" ? <LoginRegister callbackSetViewerId={ setViewerId } /> : null }
      { page === "ViewerStats" ? <ViewerStats viewerId={ {viewerId: viewerId} } /> : null }
    </div>
  );
}

export default App;
