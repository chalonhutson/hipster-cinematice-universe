import React, { useState } from 'react'
import '../App.css'

export default function LoginRegister({ callbackSetViewerId }) {

    const [loginUsername, setLoginUsername] = useState("")
    const [loginPassword, setLoginPassword] = useState("")
    const [loginAdminViewer, setLoginAdminViewer] = useState("Viewer")
 
    function getViewerIdFromServer(username) {
        fetch(`/get-viewer-id/${username}`)
        .then(res => res.json())
        .then(data => {
            callbackSetViewerId(data.viewer_id)
        })
    }

    function attemptLogin() {
        console.log("attempted")
        fetch('/login', {
            method: 'POST',
            body: JSON.stringify({
                username: loginUsername,
                password: loginPassword
            })
        })
            .then(res => res.json())
            .then(data => {
                console.log('Success:', data)
            })
        
    }

    return (
        <div>
            <h2>Login</h2>
            <div className="loginContainer">
                <h3>Username:</h3>
                <input type="text" onChange={(e) => setLoginUsername(e.target.value)} value={loginUsername} />
                <h3>Password:</h3>
                <input type="password" onChange={(e) => setLoginPassword(e.target.value)} value={loginPassword} />
                <div className="buttons">
                    <button 
                        className={loginAdminViewer === "Viewer" ? "buttonSelected" : "buttonUnselected"} 
                        onClick={() => {
                            setLoginAdminViewer("Viewer")
                            getViewerIdFromServer(loginUsername)
                        }
                        }
                    >
                        Viewer
                    </button>
                    <button 
                        className={loginAdminViewer === "Admin" ? "buttonSelected" : "buttonUnselected"}
                        onClick={() => setLoginAdminViewer("Admin")}
                    >
                        Admin
                    </button>
                </div>
                <button onClick={() => attemptLogin()}>Login</button>

            </div>
        </div>
    )
}
