import React, { useState, useEffect } from 'react'

export default function ViewerStats({ viewerId }) {

  const [messages, setMessages] = useState([])
  const [redemptions, setRedemptions] = useState([])

  useEffect(() => {
    fetch(`/get-messages/${viewerId.viewerId}`).then(res => res.json()).then(data => {
      setMessages(data)
    })
    
    fetch(`/get-redemptions/${viewerId.viewerId}`).then(res => res.json()).then(data => {
      setRedemptions(data)
    })
  }, [])
  
  const deliveredMessages = messages.map((i) => {
    return (
      <div key={i.message_id}>
      <h4 key={`Message ${i.message_id.toString()}`}>Message: {i.message_content}</h4>
      <h4 key={`Datetime ${i.message_id.toString()}`}>Message Date: {i.message_datetime}</h4>
    </div>
    )
  })
  
  return (
    <div>
      <div>
        <h1>Viewer Stats</h1>
        <div>
          <h2>Messages</h2>

          {console.log(`/get-messages/${viewerId.viewerId}`)}
          { deliveredMessages }
          
          
        </div>
      </div>
      <div>
        <h1>Viewer Redemptions</h1>
        <div>
          <h2>Redemptions</h2>

        </div>
      </div>
    </div>
  )
}
