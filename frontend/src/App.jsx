import { useState } from "react"
import Upload from "./components/Upload"
import Result from "./components/Result"
import Header from "./components/Header"
import "./index.css"

function App() {
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [preview, setPreview] = useState(null)

  return (
    <div className="app">
      <Header />
      <main className="container">
        <Upload
          setResult={setResult}
          setLoading={setLoading}
          setPreview={setPreview}
          loading={loading}
        />
        {(loading || result) && (
          <Result
            result={result}
            loading={loading}
            preview={preview}
          />
        )}
      </main>
    </div>
  )
}

export default App