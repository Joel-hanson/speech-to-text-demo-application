import { useState } from 'react'
import './App.css'
// import reactLogo from '/react.svg'
// import viteLogo from '/vite.svg'
// import djangoLogo from '/django.svg'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <div>
        <a href="https://www.djangoproject.com/" target="_blank">
          {/* <img src={djangoLogo} className="logo" alt="Vite logo" /> */}
          <img src={"static/django.svg"} className="logo" alt="Django logo" />
        </a>
        <a href="https://vitejs.dev" target="_blank">
          {/* <img src={viteLogo} className="logo" alt="Vite logo" /> */}
          <img src={"static/vite.svg"} className="logo" alt="Vite logo" />
        </a>
        <a href="https://reactjs.org" target="_blank">
          {/* <img src={reactLogo} className="logo react" alt="React logo" /> */}
          <img src={"static/react.svg"} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Django + Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </div>
  )
}

export default App
